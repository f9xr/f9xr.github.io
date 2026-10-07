#!/usr/bin/env node
/**
 * Re-pulls the Google Sheets CSV sources used by the directory listing pages
 * and writes them to directories/data/<slug>.csv.
 *
 * The Google Sheet remains the source of truth; the site ships local snapshots
 * so pages do not depend on docs.google.com at runtime.
 *
 * Usage: npm run refresh:data
 */
const fs = require('fs');
const path = require('path');

const ROOT = path.join(__dirname, '..');
const OUT_DIR = path.join(ROOT, 'directories', 'data');

const SHEETS = {
  'ai-tools': '1Hr3oGmWGUZPO4wgtmb7bDQBgZcB-RtzCuNDpMDA6l8Q',
  'business-listing-sites': '1xq5nBZRxxO0hmFTT_sybWRHs7SuRBXrUeBUoftFwCqc',
  'forum-posting-sites': '1L66EZD-CgLOv1hjuZNOYDNV1RcYdGXo_LQvpvYcCyeY',
  'free-backlink-creation-sites': '1ihfagbGoGyCA02wHc1VmDiUpYEZkmzkQZra86CKv8GA',
  'pdf-submission-portals': '1CPL52fmsdh9XTOBuZifcSUrv4BcLmTv9UzqF6nyRv7Q',
  'product-launch-directories': '1hQaYa19LsIVERZa5ubRv7ZVlRLqrF_d3Stih9VllEI0',
  'project-submission-sites': '1Ij4Q1eYAbqFW8R-FguKLNqqEdzQcF_EE81FRWg63l7M',
  'skill-listing-directory': '1O9ZcJCWTby7PDcRP5Hk03yh-ZBao2ngCpxMG4mDvdYU',
  'web2-submission-sites': '135iqVxSEWpmuDMyB08X5mN2EqY2GYayHZqZ_U_J5P2Y'
};

global.window = {};
require(path.join(ROOT, 'assets', 'js', 'directories.js'));
const { dataRows } = global.window.F9XRDirs;

function sheetUrl(id) {
  return 'https://docs.google.com/spreadsheets/d/' + id + '/gviz/tq?tqx=out:csv';
}

function rowStats(csv) {
  const rows = dataRows(csv);
  const widths = {};
  rows.forEach(r => { widths[r.length] = (widths[r.length] || 0) + 1; });
  return { rows: rows.length, widths };
}

async function refresh(slug, id) {
  const file = path.join(OUT_DIR, slug + '.csv');
  const res = await fetch(sheetUrl(id), { redirect: 'follow' });
  if (!res.ok) throw new Error('HTTP ' + res.status);
  let csv = (await res.text()).replace(/^\uFEFF/, '');
  if (!csv.trim()) throw new Error('empty response');
  const next = rowStats(csv);
  const prev = fs.existsSync(file) ? rowStats(fs.readFileSync(file, 'utf8')) : { rows: 0, widths: {} };
  if (next.rows === 0) throw new Error('no data rows parsed');
  fs.writeFileSync(file, csv);
  const flag = next.rows < prev.rows ? '  <-- FEWER ROWS THAN BEFORE' : '';
  console.log(
    slug + ': ' + prev.rows + ' -> ' + next.rows + ' rows, cols ' +
    JSON.stringify(next.widths) + flag
  );
}

(async function main() {
  if (!fs.existsSync(OUT_DIR)) fs.mkdirSync(OUT_DIR, { recursive: true });
  const failures = [];
  for (const [slug, id] of Object.entries(SHEETS)) {
    try {
      await refresh(slug, id);
    } catch (e) {
      failures.push(slug + ' (' + e.message + ')');
      console.error(slug + ': FAILED - ' + e.message);
    }
  }
  if (failures.length) {
    console.error('\n' + failures.length + ' sheet(s) failed; existing snapshots kept.');
    process.exit(1);
  }
  console.log('\nAll directory snapshots refreshed.');
})();
