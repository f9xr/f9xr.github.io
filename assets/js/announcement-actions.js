(function () {
  "use strict";

  function getAnnouncementData() {
    var h1 = document.querySelector("h1");
    var header = document.querySelector(".mb-12.border-b");
    var metaEl = header ? header.querySelector('div[class*="tracking-widest"]') : null;
    var article = document.querySelector("article");

    var title = h1 ? h1.innerText.replace(/\s+/g, " ").trim() : document.title;
    var meta = metaEl ? metaEl.innerText.replace(/\s+/g, " ").trim() : "";
    var body = article ? article.innerText.replace(/\s+/g, " ").trim() : "";
    var source = window.location.href;

    return { title: title, meta: meta, body: body, source: source };
  }

  function showToast(msg) {
    var existing = document.getElementById("f9xr-announcement-toast");
    if (existing) existing.remove();
    var t = document.createElement("div");
    t.id = "f9xr-announcement-toast";
    t.textContent = msg;
    t.setAttribute("role", "status");
    t.style.cssText =
      "position:fixed;bottom:24px;left:50%;transform:translateX(-50%);background:#3b82f6;color:#fff;padding:12px 24px;border-radius:9999px;font-weight:700;font-size:14px;z-index:9999;box-shadow:0 10px 30px rgba(0,0,0,0.4);transition:opacity .3s";
    document.body.appendChild(t);
    setTimeout(function () {
      t.style.opacity = "0";
      setTimeout(function () { t.remove(); }, 350);
    }, 2200);
  }

  window.copyAnnouncement = function () {
    var d = getAnnouncementData();
    var text = d.title + "\n" + d.meta + "\n\n" + d.body + "\n\nSource: " + d.source;
    var onDone = function () { showToast("Announcement copied to clipboard"); };
    var onFail = function () { showToast("Could not copy automatically"); };

    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(onDone, onFail);
      return;
    }
    var ta = document.createElement("textarea");
    ta.value = text;
    ta.style.cssText = "position:fixed;opacity:0;top:0;left:0";
    document.body.appendChild(ta);
    ta.focus();
    ta.select();
    try {
      document.execCommand("copy");
      onDone();
    } catch (e) {
      onFail();
    }
    document.body.removeChild(ta);
  };

  window.downloadAnnouncementPdf = function () {
    var d = getAnnouncementData();
    var JsPDF = window.jspdf ? window.jspdf.jsPDF : null;
    if (!JsPDF) {
      showToast("PDF library still loading, please try again");
      return;
    }

    var doc = new JsPDF({ unit: "pt", format: "a4" });
    var pageW = doc.internal.pageSize.getWidth();
    var pageH = doc.internal.pageSize.getHeight();
    var margin = 56;
    var maxW = pageW - margin * 2;
    var y = margin;
    var lineH = 15;

    function ensureSpace(needed) {
      if (y + needed > pageH - margin) {
        doc.addPage();
        y = margin;
      }
    }

    doc.setFont("helvetica", "bold");
    doc.setFontSize(19);
    doc.setTextColor(24, 25, 28);
    var titleLines = doc.splitTextToSize(d.title, maxW);
    for (var i = 0; i < titleLines.length; i++) {
      ensureSpace(lineH + 8);
      doc.text(titleLines[i], margin, y);
      y += lineH + 8;
    }

    y += 6;
    doc.setFont("helvetica", "normal");
    doc.setFontSize(9.5);
    doc.setTextColor(130, 130, 140);
    var metaLines = doc.splitTextToSize(d.meta + "  |  Source: " + d.source, maxW);
    for (var j = 0; j < metaLines.length; j++) {
      doc.text(metaLines[j], margin, y);
      y += 13;
    }

    y += 12;
    doc.setFont("helvetica", "normal");
    doc.setFontSize(10.5);
    doc.setTextColor(40, 40, 45);
    var bodyLines = doc.splitTextToSize(d.body, maxW);
    for (var k = 0; k < bodyLines.length; k++) {
      ensureSpace(lineH);
      doc.text(bodyLines[k], margin, y);
      y += lineH;
    }

    var pages = doc.internal.getNumberOfPages();
    doc.setFontSize(9);
    doc.setTextColor(150, 150, 155);
    for (var p = 1; p <= pages; p++) {
      doc.setPage(p);
      doc.text("F9XR Team Announcement", pageW / 2, pageH - 30, { align: "center" });
      doc.text(p + " / " + pages, pageW - margin, pageH - 30, { align: "right" });
    }

    var file = d.title.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60) || "f9xr-announcement";
    doc.save(file + ".pdf");
  };
})();
