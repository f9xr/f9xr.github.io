(function (global) {
  'use strict';

  function parseCSV(text) {
    var rows = [], row = [], field = '', inQuotes = false, i, c;
    text = String(text == null ? '' : text).replace(/^\uFEFF/, '');
    for (i = 0; i < text.length; i++) {
      c = text.charAt(i);
      if (inQuotes) {
        if (c === '"') {
          if (text.charAt(i + 1) === '"') { field += '"'; i++; } else { inQuotes = false; }
        } else { field += c; }
      } else if (c === '"') {
        inQuotes = true;
      } else if (c === ',') {
        row.push(field); field = '';
      } else if (c === '\n') {
        row.push(field); rows.push(row); row = []; field = '';
      } else if (c !== '\r') {
        field += c;
      }
    }
    if (field !== '' || row.length) { row.push(field); rows.push(row); }
    return rows;
  }

  function dataRows(text) {
    return parseCSV(text).slice(1).filter(function (r) {
      return r.join('').trim() !== '';
    });
  }

  function absUrl(url) {
    url = String(url == null ? '' : url).trim();
    if (!url) return '';
    if (!/^https?:\/\//i.test(url)) url = 'https://' + url;
    return url;
  }

  function host(url) {
    return String(url == null ? '' : url)
      .trim()
      .replace(/^https?:\/\//i, '')
      .replace(/^www\./i, '')
      .replace(/[/?#].*$/, '')
      .replace(/\/+$/, '');
  }

  function uniqBy(list, keyFn) {
    var seen = {}, out = [];
    for (var i = 0; i < list.length; i++) {
      var key = keyFn(list[i]);
      if (!key || seen[key]) continue;
      seen[key] = true;
      out.push(list[i]);
    }
    return out;
  }

  function esc(value) {
    return String(value == null ? '' : value)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  function pager(containerId, page, totalPages, onChange) {
    var container = document.getElementById(containerId);
    if (!container) return;
    if (!totalPages || totalPages <= 1) { container.innerHTML = ''; return; }
    var btn = 'px-3 py-2 rounded-lg text-xs font-bold transition-all border cursor-pointer ';
    var idle = 'bg-white/5 border-white/10 text-white/70 hover:bg-white/10';
    var active = 'bg-accent-blue border-accent-blue text-white';
    var html = '<button type="button" data-page="' + (page - 1) + '" ' + (page === 1 ? 'disabled' : '') + ' aria-label="Previous page" class="' + btn + idle + ' disabled:opacity-30 disabled:cursor-not-allowed"><i class="fa-solid fa-chevron-left"></i></button>';
    var start = Math.max(1, page - 2);
    var end = Math.min(totalPages, page + 2);
    if (start > 1) {
      html += '<button type="button" data-page="1" class="' + btn + idle + '">1</button>';
      if (start > 2) html += '<span class="text-white/30 text-xs px-1">...</span>';
    }
    for (var i = start; i <= end; i++) {
      html += '<button type="button" data-page="' + i + '" ' + (i === page ? 'aria-current="page"' : '') + ' class="' + btn + (i === page ? active : idle) + '">' + i + '</button>';
    }
    if (end < totalPages) {
      if (end < totalPages - 1) html += '<span class="text-white/30 text-xs px-1">...</span>';
      html += '<button type="button" data-page="' + totalPages + '" class="' + btn + idle + '">' + totalPages + '</button>';
    }
    html += '<button type="button" data-page="' + (page + 1) + '" ' + (page === totalPages ? 'disabled' : '') + ' aria-label="Next page" class="' + btn + idle + ' disabled:opacity-30 disabled:cursor-not-allowed"><i class="fa-solid fa-chevron-right"></i></button>';
    container.innerHTML = html;
    container.onclick = function (event) {
      var target = event.target && event.target.closest ? event.target.closest('[data-page]') : null;
      if (!target || target.disabled) return;
      var next = parseInt(target.getAttribute('data-page'), 10);
      if (!isNaN(next) && next >= 1 && next <= totalPages) onChange(next);
    };
  }

  function slice(data, page, perPage) {
    var start = (page - 1) * perPage;
    return data.slice(start, start + perPage);
  }

  function pageCount(total, perPage) {
    return Math.max(1, Math.ceil(total / perPage));
  }

  global.F9XRDirs = {
    parseCSV: parseCSV,
    dataRows: dataRows,
    absUrl: absUrl,
    host: host,
    uniqBy: uniqBy,
    esc: esc,
    pager: pager,
    slice: slice,
    pageCount: pageCount
  };
})(window);
