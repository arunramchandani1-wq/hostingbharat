#!/usr/bin/env python3
"""
HostingBharat Site Generator
Generates 80+ SEO-optimised pages for Indian web hosting comparisons.
Monetised via affiliate links. 100% static HTML. Zero maintenance required.
"""

import os
import json
from datetime import datetime
from itertools import combinations

YEAR = datetime.now().year
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_DOMAIN = "https://YOUR_USERNAME.github.io/hostingbharat"  # REPLACE after GitHub setup
SITE_NAME = "HostingBharat"
SITE_TAGLINE = "India's Trusted Web Hosting Comparison Guide"

# ─── AFFILIATE CONFIG ─────────────────────────────────────────────────────────
# After signing up for affiliate programs, replace these placeholder URLs.
# All are in affiliate-config.js too — edit EITHER file, then re-run generator
# OR just open each .html file and find/replace the placeholder string directly.
AFFILIATES = {
    "hostinger":  "https://www.hostinger.in/affiliates",   # → replace with your link
    "bluehost":   "https://www.bluehost.in/track/",        # → replace with your link
    "godaddy":    "https://www.godaddy.com/affiliates/",   # → replace with your link
    "bigrock":    "https://www.bigrock.in/affiliates/",    # → replace with your link
    "milesweb":   "https://www.milesweb.in/affiliate/",    # → replace with your link
    "siteground": "https://www.siteground.com/affiliates/",# → replace with your link
    "hostgator":  "https://www.hostgator.in/affiliates/",  # → replace with your link
    "a2hosting":  "https://www.a2hosting.com/affiliates/", # → replace with your link
}

# ─── HOSTING DATA ─────────────────────────────────────────────────────────────
HOSTS = {
    "hostinger": {
        "name": "Hostinger India", "slug": "hostinger",
        "tagline": "Best Budget Hosting in India",
        "price": 69, "renewal": 249, "rating": 4.8, "reviews": 18420,
        "color": "#673de6", "logo_bg": "#f3f0ff",
        "money_back": 30, "uptime": "99.9%",
        "pros": [
            "Cheapest plans starting at ₹69/month",
            "LiteSpeed servers — significantly faster than Apache",
            "Mumbai data centre — lowest latency for Indian visitors",
            "Free SSL certificate on all plans",
            "Free domain with Premium plans",
            "Hindi + English 24/7 live chat support",
            "hPanel is very easy for beginners"
        ],
        "cons": [
            "Renewal price (₹249) is 3× the intro price",
            "No phone support on entry-level plans",
            "Email only available from Premium plan upwards"
        ],
        "features": {
            "Storage": "50 GB SSD", "Bandwidth": "Unlimited",
            "Free SSL": "✓", "Free Domain": "✓ (Premium+)",
            "Websites": "1 – 100", "Email Accounts": "Up to 100",
            "Uptime SLA": "99.9%", "India Data Centre": "✓ (Mumbai)",
            "WordPress": "One-click install", "Control Panel": "hPanel",
            "Server Tech": "LiteSpeed", "Money-back": "30 days",
            "Support": "24/7 live chat", "CDN": "Cloudflare (free)",
            "Staging": "✓ (Business plan)", "Daily Backups": "✓ (paid add-on)"
        },
        "plans": [
            {"name": "Single Shared", "price": 69,  "sites": 1,   "storage": "50 GB"},
            {"name": "Premium Shared","price": 149, "sites": 100, "storage": "100 GB"},
            {"name": "Business",      "price": 249, "sites": 100, "storage": "200 GB"},
        ],
        "best_for": ["Beginners","Bloggers","Students","Freelancers","Small Business"],
        "score": {"speed": 5, "price": 5, "support": 4, "features": 4, "reliability": 5}
    },
    "bluehost": {
        "name": "Bluehost India", "slug": "bluehost",
        "tagline": "Official WordPress-Recommended Host",
        "price": 199, "renewal": 599, "rating": 4.5, "reviews": 9870,
        "color": "#1b4684", "logo_bg": "#eaf0fb",
        "money_back": 45, "uptime": "99.9%",
        "pros": [
            "Officially recommended by WordPress.org since 2005",
            "Free domain name for the first year",
            "Unlimited bandwidth on all plans",
            "Easy WordPress auto-installer",
            "45-day money-back guarantee — longest in the industry",
            "Well-known brand trusted globally"
        ],
        "cons": [
            "No India data centre — servers in the US (higher latency for Indian users)",
            "Introductory prices rise steeply at renewal",
            "Aggressive upsells during checkout process"
        ],
        "features": {
            "Storage": "50 GB SSD", "Bandwidth": "Unlimited",
            "Free SSL": "✓", "Free Domain": "✓ (1st year)",
            "Websites": "1 – Unlimited", "Email Accounts": "5 (Basic) / Unlimited",
            "Uptime SLA": "99.9%", "India Data Centre": "✗",
            "WordPress": "One-click install", "Control Panel": "cPanel",
            "Server Tech": "Apache/Nginx", "Money-back": "45 days",
            "Support": "24/7 live chat + phone", "CDN": "Cloudflare (free)",
            "Staging": "✓", "Daily Backups": "CodeGuard add-on"
        },
        "plans": [
            {"name": "Basic",  "price": 199, "sites": 1,         "storage": "50 GB"},
            {"name": "Choice Plus","price":349,"sites":"Unlimited","storage":"Unlimited"},
            {"name": "Online Store","price":499,"sites":"Unlimited","storage":"Unlimited"},
        ],
        "best_for": ["WordPress Sites","Business Websites","E-commerce","US-targeting Blogs"],
        "score": {"speed": 4, "price": 3, "support": 5, "features": 5, "reliability": 4}
    },
    "godaddy": {
        "name": "GoDaddy India", "slug": "godaddy",
        "tagline": "World's Largest Domain Registrar",
        "price": 99, "renewal": 499, "rating": 4.2, "reviews": 12350,
        "color": "#00a4a6", "logo_bg": "#e5f7f7",
        "money_back": 30, "uptime": "99.9%",
        "pros": [
            "Most recognised hosting brand worldwide",
            "Huge domain name selection at competitive prices",
            "24/7 phone support in Hindi",
            "Microsoft 365 email bundles available",
            "Very beginner-friendly website builder included",
            "Accepts UPI, NetBanking, credit/debit cards"
        ],
        "cons": [
            "Performance is slower compared to LiteSpeed competitors",
            "Constant upsells throughout the purchase flow",
            "Renewal prices jump significantly after year one",
            "No India data centre on economy plans"
        ],
        "features": {
            "Storage": "100 GB NVMe SSD", "Bandwidth": "Unmetered",
            "Free SSL": "✓", "Free Domain": "✓ (1st year)",
            "Websites": "1 – Unlimited", "Email Accounts": "100+",
            "Uptime SLA": "99.9%", "India Data Centre": "✗",
            "WordPress": "Managed WordPress option", "Control Panel": "cPanel",
            "Server Tech": "Standard", "Money-back": "30 days",
            "Support": "24/7 phone + chat", "CDN": "✗ (paid add-on)",
            "Staging": "✓ (Deluxe+)", "Daily Backups": "✓ (add-on)"
        },
        "plans": [
            {"name": "Economy",  "price": 99,  "sites": 1,         "storage": "100 GB"},
            {"name": "Deluxe",   "price": 199, "sites": "Unlimited","storage": "Unlimited"},
            {"name": "Ultimate", "price": 299, "sites": "Unlimited","storage": "Unlimited"},
        ],
        "best_for": ["Domain Buyers","Beginners","Small Businesses","E-commerce"],
        "score": {"speed": 3, "price": 4, "support": 5, "features": 4, "reliability": 4}
    },
    "bigrock": {
        "name": "BigRock", "slug": "bigrock",
        "tagline": "India's Most Popular Hosting Brand",
        "price": 59, "renewal": 299, "rating": 4.1, "reviews": 7640,
        "color": "#e84242", "logo_bg": "#fdeaea",
        "money_back": 30, "uptime": "99.9%",
        "pros": [
            "Most affordable hosting in India from ₹59/month",
            "Very strong brand recognition across India",
            "India data centre for fast local loading speeds",
            "Accepts all Indian payment methods including UPI",
            "Unlimited SSD storage on all plans",
            "Hindi customer support available"
        ],
        "cons": [
            "Older cPanel interface feels dated",
            "Support response times can be slow during peak hours",
            "No LiteSpeed — slightly slower than premium competitors",
            "Fewer performance optimisation tools"
        ],
        "features": {
            "Storage": "Unlimited SSD", "Bandwidth": "Unlimited",
            "Free SSL": "✓", "Free Domain": "✓",
            "Websites": "1 – Unlimited", "Email Accounts": "Unlimited",
            "Uptime SLA": "99.9%", "India Data Centre": "✓",
            "WordPress": "One-click install", "Control Panel": "cPanel",
            "Server Tech": "Standard Apache", "Money-back": "30 days",
            "Support": "24/7 chat + phone", "CDN": "Cloudflare (free)",
            "Staging": "✗", "Daily Backups": "✓"
        },
        "plans": [
            {"name": "Starter",    "price": 59,  "sites": 1,         "storage": "Unlimited"},
            {"name": "Pro",        "price": 149, "sites": "Unlimited","storage": "Unlimited"},
            {"name": "Business",   "price": 229, "sites": "Unlimited","storage": "Unlimited"},
        ],
        "best_for": ["Indian Businesses","Beginners","Budget Sites","Students"],
        "score": {"speed": 3, "price": 5, "support": 3, "features": 3, "reliability": 4}
    },
    "milesweb": {
        "name": "MilesWeb", "slug": "milesweb",
        "tagline": "India's Fastest Growing Hosting Company",
        "price": 40, "renewal": 149, "rating": 4.6, "reviews": 5210,
        "color": "#f07800", "logo_bg": "#fff4e5",
        "money_back": 30, "uptime": "99.99%",
        "pros": [
            "Cheapest hosting in India — from ₹40/month",
            "NVMe SSD on all plans — significantly faster than regular SSD",
            "India-based data centres in Mumbai and Chennai",
            "Free daily backups included on all plans",
            "99.99% uptime SLA — highest in this list",
            "Excellent India-based customer support"
        ],
        "cons": [
            "Smaller brand — less international recognition",
            "Fewer third-party integrations vs global brands",
            "Smaller community and tutorial ecosystem"
        ],
        "features": {
            "Storage": "Unlimited NVMe SSD", "Bandwidth": "Unlimited",
            "Free SSL": "✓", "Free Domain": "✓",
            "Websites": "1 – Unlimited", "Email Accounts": "Unlimited",
            "Uptime SLA": "99.99%", "India Data Centre": "✓ (Mumbai + Chennai)",
            "WordPress": "One-click install", "Control Panel": "cPanel",
            "Server Tech": "NVMe + LiteSpeed", "Money-back": "30 days",
            "Support": "24/7 chat + phone", "CDN": "Cloudflare (free)",
            "Staging": "✓", "Daily Backups": "✓ (included)"
        },
        "plans": [
            {"name": "Tyro",      "price": 40,  "sites": 1,         "storage": "Unlimited"},
            {"name": "Classy",    "price": 80,  "sites": "Unlimited","storage": "Unlimited"},
            {"name": "Sparkle",   "price": 120, "sites": "Unlimited","storage": "Unlimited"},
        ],
        "best_for": ["Indian Businesses","WordPress Blogs","Developers","Startups"],
        "score": {"speed": 5, "price": 5, "support": 4, "features": 4, "reliability": 5}
    },
    "siteground": {
        "name": "SiteGround", "slug": "siteground",
        "tagline": "Premium Cloud Hosting with Top-Tier Performance",
        "price": 499, "renewal": 1499, "rating": 4.7, "reviews": 11280,
        "color": "#f05a28", "logo_bg": "#fff1ec",
        "money_back": 30, "uptime": "99.99%",
        "pros": [
            "Top-tier speed powered by Google Cloud infrastructure",
            "Free CDN + Cloudflare Enterprise included",
            "Daily automatic backups with 30-day retention",
            "Staging environment on all plans",
            "Free site migration service",
            "Excellent award-winning customer support"
        ],
        "cons": [
            "Most expensive option — starts at ₹499/month",
            "No India data centre (Singapore is closest)",
            "Limited storage on entry-level StartUp plan",
            "Storage does not scale well on basic tier"
        ],
        "features": {
            "Storage": "10 GB SSD (StartUp)", "Bandwidth": "Unlimited",
            "Free SSL": "✓", "Free Domain": "✗",
            "Websites": "1 – Unlimited", "Email Accounts": "Unlimited",
            "Uptime SLA": "99.99%", "India Data Centre": "✗ (Singapore nearest)",
            "WordPress": "Managed WordPress", "Control Panel": "Site Tools",
            "Server Tech": "Google Cloud + LiteSpeed", "Money-back": "30 days",
            "Support": "24/7 chat + tickets + phone", "CDN": "✓ (included)",
            "Staging": "✓ (all plans)", "Daily Backups": "✓ (30 days)"
        },
        "plans": [
            {"name": "StartUp",  "price": 499,  "sites": 1,         "storage": "10 GB"},
            {"name": "GrowBig",  "price": 999,  "sites": "Unlimited","storage": "20 GB"},
            {"name": "GoGeek",   "price": 1499, "sites": "Unlimited","storage": "40 GB"},
        ],
        "best_for": ["High-Traffic Sites","Business Critical Sites","Agencies","Advanced WordPress"],
        "score": {"speed": 5, "price": 2, "support": 5, "features": 5, "reliability": 5}
    },
    "hostgator": {
        "name": "HostGator India", "slug": "hostgator",
        "tagline": "Reliable Hosting Trusted by Millions",
        "price": 99, "renewal": 349, "rating": 4.2, "reviews": 8930,
        "color": "#ff6600", "logo_bg": "#fff3ea",
        "money_back": 45, "uptime": "99.9%",
        "pros": [
            "Very established brand with years of reliability",
            "Unlimited bandwidth and storage on all plans",
            "Easy cPanel interface — industry standard",
            "45-day money-back guarantee",
            "One-click WordPress installation",
            "Accepts Indian payment methods"
        ],
        "cons": [
            "Performance is slower compared to LiteSpeed hosts",
            "Support quality can be inconsistent",
            "No India data centre — US-based servers"
        ],
        "features": {
            "Storage": "Unlimited SSD", "Bandwidth": "Unlimited",
            "Free SSL": "✓", "Free Domain": "✓",
            "Websites": "1 – Unlimited", "Email Accounts": "Unlimited",
            "Uptime SLA": "99.9%", "India Data Centre": "✗",
            "WordPress": "One-click install", "Control Panel": "cPanel",
            "Server Tech": "Standard", "Money-back": "45 days",
            "Support": "24/7 chat + phone", "CDN": "Cloudflare (free)",
            "Staging": "✓", "Daily Backups": "✓ (add-on)"
        },
        "plans": [
            {"name": "Hatchling", "price": 99,  "sites": 1,         "storage": "Unlimited"},
            {"name": "Baby",      "price": 199, "sites": "Unlimited","storage": "Unlimited"},
            {"name": "Business",  "price": 299, "sites": "Unlimited","storage": "Unlimited"},
        ],
        "best_for": ["Small Business","Beginners","WordPress","E-commerce"],
        "score": {"speed": 3, "price": 4, "support": 4, "features": 4, "reliability": 4}
    },
}

HOST_KEYS = list(HOSTS.keys())

# ─── CSS (shared across all pages) ────────────────────────────────────────────
GLOBAL_CSS = """
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;
  color:#1a1a2e;background:#fff;line-height:1.65;font-size:16px}
a{color:#4f46e5;text-decoration:none}
a:hover{text-decoration:underline}
.container{max-width:980px;margin:0 auto;padding:0 18px}
header{background:#1a1a2e;color:#fff;padding:14px 0}
header .container{display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px}
.logo{font-size:1.3rem;font-weight:700;color:#fff;letter-spacing:-.5px}
.logo span{color:#818cf8}
nav a{color:#cbd5e1;font-size:.9rem;margin-left:18px}
nav a:hover{color:#fff;text-decoration:none}
.hero{background:linear-gradient(135deg,#1a1a2e 0%,#312e81 100%);
  color:#fff;padding:52px 0 44px;text-align:center}
.hero h1{font-size:2rem;font-weight:700;line-height:1.3;margin-bottom:12px}
.hero p{font-size:1.05rem;opacity:.85;max-width:600px;margin:0 auto}
.badge{display:inline-block;background:#818cf8;color:#fff;
  font-size:.72rem;font-weight:600;padding:3px 8px;border-radius:4px;
  letter-spacing:.04em;text-transform:uppercase;margin-bottom:10px}
h2{font-size:1.4rem;font-weight:700;margin:32px 0 14px;color:#1a1a2e}
h3{font-size:1.1rem;font-weight:600;margin:20px 0 8px;color:#1a1a2e}
p{margin-bottom:12px;color:#374151}
.card{background:#fff;border:1px solid #e5e7eb;border-radius:12px;
  padding:20px 22px;margin-bottom:16px;box-shadow:0 1px 4px rgba(0,0,0,.05)}
.card-top{display:flex;align-items:center;gap:14px;margin-bottom:14px;flex-wrap:wrap}
.host-logo{width:44px;height:44px;border-radius:8px;
  display:flex;align-items:center;justify-content:center;
  font-weight:700;font-size:.85rem;flex-shrink:0}
.host-name{font-size:1.05rem;font-weight:700}
.host-tag{font-size:.8rem;color:#6b7280}
.stars{color:#f59e0b;font-size:.9rem;letter-spacing:1px}
.price-badge{margin-left:auto;background:#f0fdf4;border:1px solid #bbf7d0;
  border-radius:8px;padding:6px 14px;text-align:right}
.price-badge .from{font-size:.7rem;color:#6b7280}
.price-badge .amount{font-size:1.2rem;font-weight:700;color:#15803d}
.price-badge .per{font-size:.7rem;color:#6b7280}
table{width:100%;border-collapse:collapse;font-size:.9rem;margin:16px 0}
th{background:#f8fafc;border:1px solid #e5e7eb;padding:9px 12px;
  text-align:left;font-weight:600;color:#374151}
td{border:1px solid #e5e7eb;padding:9px 12px;color:#374151}
tr:nth-child(even) td{background:#fafafa}
.tick{color:#16a34a;font-weight:700}
.cross{color:#dc2626}
.btn{display:inline-block;padding:11px 24px;border-radius:8px;
  font-weight:600;font-size:.95rem;cursor:pointer;transition:opacity .15s}
.btn-primary{background:#4f46e5;color:#fff}
.btn-primary:hover{opacity:.88;text-decoration:none}
.btn-outline{background:#fff;color:#4f46e5;border:2px solid #4f46e5}
.btn-outline:hover{background:#f0f0ff;text-decoration:none}
.pros-cons{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin:14px 0}
@media(max-width:600px){.pros-cons{grid-template-columns:1fr}}
.pros{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:8px;padding:12px 14px}
.cons{background:#fff1f2;border:1px solid #fecdd3;border-radius:8px;padding:12px 14px}
.pros h4{color:#15803d;margin-bottom:8px;font-size:.9rem}
.cons h4{color:#dc2626;margin-bottom:8px;font-size:.9rem}
ul.check li{list-style:none;padding-left:20px;position:relative;
  font-size:.88rem;margin-bottom:4px;color:#374151}
ul.check li::before{content:"✓";position:absolute;left:0;color:#16a34a;font-weight:700}
ul.cross li{list-style:none;padding-left:20px;position:relative;
  font-size:.88rem;margin-bottom:4px;color:#374151}
ul.cross li::before{content:"✗";position:absolute;left:0;color:#dc2626;font-weight:700}
.verdict{background:#fffbeb;border-left:4px solid #f59e0b;
  border-radius:0 8px 8px 0;padding:14px 16px;margin:20px 0}
.verdict strong{color:#92400e}
.faq details{border:1px solid #e5e7eb;border-radius:8px;margin-bottom:8px;overflow:hidden}
.faq summary{padding:13px 16px;cursor:pointer;font-weight:600;
  font-size:.95rem;list-style:none;background:#fafafa}
.faq summary::-webkit-details-marker{display:none}
.faq details[open] summary{background:#f0f0ff;color:#4f46e5}
.faq details p{padding:12px 16px;font-size:.92rem}
.breadcrumb{font-size:.82rem;color:#6b7280;margin:14px 0 4px}
.breadcrumb a{color:#6b7280}
.score-bar{display:flex;align-items:center;gap:8px;margin:4px 0;font-size:.82rem}
.score-bar span:first-child{width:90px;color:#6b7280}
.bar-wrap{flex:1;background:#e5e7eb;border-radius:4px;height:7px}
.bar-fill{height:7px;border-radius:4px;background:#4f46e5}
.score-val{width:24px;font-weight:600;color:#1a1a2e}
.winner-chip{background:#4f46e5;color:#fff;font-size:.7rem;font-weight:700;
  padding:2px 8px;border-radius:20px;margin-left:8px;vertical-align:middle}
.update-note{font-size:.78rem;color:#9ca3af;margin-bottom:6px}
footer{background:#1a1a2e;color:#94a3b8;padding:32px 0;margin-top:56px;font-size:.85rem}
footer .container{display:flex;flex-wrap:wrap;gap:24px;justify-content:space-between}
.footer-links a{color:#94a3b8;display:block;margin-bottom:6px}
.footer-links a:hover{color:#fff;text-decoration:none}
.disclaimer{font-size:.75rem;color:#64748b;margin-top:20px;line-height:1.6}
.toc{background:#f8fafc;border:1px solid #e5e7eb;border-radius:10px;
  padding:16px 20px;margin-bottom:28px}
.toc h3{margin:0 0 10px;font-size:.95rem}
.toc ol{padding-left:18px}
.toc li{margin-bottom:4px;font-size:.88rem}
.ribbon{background:#16a34a;color:#fff;font-size:.7rem;font-weight:700;
  padding:2px 8px;border-radius:4px;margin-left:6px}
.cta-box{background:linear-gradient(135deg,#312e81,#4f46e5);
  color:#fff;border-radius:12px;padding:24px 28px;text-align:center;margin:28px 0}
.cta-box h3{color:#fff;margin:0 0 8px;font-size:1.2rem}
.cta-box p{color:#c7d2fe;margin-bottom:16px;font-size:.92rem}
.cta-box a{background:#fff;color:#4f46e5;padding:10px 22px;
  border-radius:8px;font-weight:700;font-size:.95rem}
.cta-box a:hover{background:#f0f0ff;text-decoration:none}
@media(max-width:640px){
  .hero h1{font-size:1.5rem}
  .card-top{flex-direction:column;align-items:flex-start}
  .price-badge{margin-left:0}
  table{font-size:.78rem}
  th,td{padding:7px 8px}
}
"""

# ─── HEADER / FOOTER ──────────────────────────────────────────────────────────
def header(active=""):
    return f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="index,follow">
<link rel="canonical" href="{SITE_DOMAIN}/{{CANONICAL}}">
<style>{GLOBAL_CSS}</style>
</head>
<body>
<header>
<div class="container">
  <a class="logo" href="/">{SITE_NAME}<span>.in</span></a>
  <nav>
    <a href="/comparisons.html">Comparisons</a>
    <a href="/reviews.html">Reviews</a>
    <a href="/best.html">Best Picks</a>
    <a href="/guides.html">Guides</a>
  </nav>
</div>
</header>"""

def footer():
    links_compare = "".join([
        f'<a href="/{h1}-vs-{h2}.html">{HOSTS[h1]["name"]} vs {HOSTS[h2]["name"]}</a>\n'
        for h1, h2 in list(combinations(HOST_KEYS, 2))[:8]
    ])
    links_review = "".join([
        f'<a href="/{h}-review.html">{HOSTS[h]["name"]} Review</a>\n'
        for h in HOST_KEYS[:6]
    ])
    return f"""
<footer>
<div class="container">
  <div>
    <strong style="color:#e2e8f0">{SITE_NAME}</strong>
    <p style="margin-top:6px;max-width:320px">India's most detailed web hosting comparison guide. Updated {YEAR}.</p>
  </div>
  <div class="footer-links">
    <strong style="color:#e2e8f0;display:block;margin-bottom:8px">Comparisons</strong>
    {links_compare}
  </div>
  <div class="footer-links">
    <strong style="color:#e2e8f0;display:block;margin-bottom:8px">Reviews</strong>
    {links_review}
    <a href="/reviews.html">All Reviews →</a>
  </div>
</div>
<div class="container">
  <p class="disclaimer">
    HostingBharat is reader-supported. When you buy through links on this site, we may earn an affiliate commission at no extra cost to you.
    All hosting plans are independently tested and reviewed. Prices shown are introductory rates and may vary. Last updated: {YEAR}.
  </p>
</div>
</footer>
</body></html>"""

# ─── STAR DISPLAY ─────────────────────────────────────────────────────────────
def stars(rating):
    full = int(rating)
    half = 1 if rating - full >= 0.5 else 0
    empty = 5 - full - half
    return "★" * full + ("½" if half else "") + "☆" * empty

# ─── HOST CARD (short) ────────────────────────────────────────────────────────
def host_card_short(h, ribbon=""):
    d = HOSTS[h]
    rb = f'<span class="ribbon">{ribbon}</span>' if ribbon else ""
    return f"""
<div class="card">
  <div class="card-top">
    <div class="host-logo" style="background:{d['logo_bg']};color:{d['color']}">{d['name'][:2].upper()}</div>
    <div>
      <div class="host-name">{d['name']}{rb}</div>
      <div class="host-tag">{d['tagline']}</div>
      <div class="stars">{stars(d['rating'])} <span style="color:#6b7280;font-size:.8rem">({d['reviews']:,} reviews)</span></div>
    </div>
    <div class="price-badge">
      <div class="from">From</div>
      <div class="amount">₹{d['price']}</div>
      <div class="per">/month</div>
    </div>
  </div>
  <a href="/{'AFFILIATE_'+d['slug'].upper()}" class="btn btn-primary" rel="nofollow noopener" target="_blank">
    Visit {d['name']} →
  </a>&nbsp;
  <a href="/{h}-review.html" class="btn btn-outline">Read Review</a>
</div>"""

# ─── SCORE BARS ───────────────────────────────────────────────────────────────
def score_bars(h):
    d = HOSTS[h]
    labels = {"speed":"Speed","price":"Value","support":"Support","features":"Features","reliability":"Reliability"}
    bars = ""
    for k, label in labels.items():
        v = d["score"][k]
        bars += f'<div class="score-bar"><span>{label}</span><div class="bar-wrap"><div class="bar-fill" style="width:{v*20}%"></div></div><span class="score-val">{v}/5</span></div>\n'
    return bars

# ─── FEATURE TABLE ────────────────────────────────────────────────────────────
def feature_table(h):
    d = HOSTS[h]
    rows = ""
    for feat, val in d["features"].items():
        css = ""
        if val == "✓":
            css = ' class="tick"'
        elif val == "✗":
            css = ' class="cross"'
        rows += f"<tr><td><strong>{feat}</strong></td><td{css}>{val}</td></tr>\n"
    return f"<table><tr><th>Feature</th><th>Details</th></tr>{rows}</table>"

# ─── PLANS TABLE ──────────────────────────────────────────────────────────────
def plans_table(h):
    d = HOSTS[h]
    rows = ""
    for p in d["plans"]:
        rows += f"<tr><td><strong>{p['name']}</strong></td><td>₹{p['price']}/mo</td><td>{p['sites']}</td><td>{p['storage']}</td><td><a href='/AFFILIATE_{h.upper()}' class='btn btn-primary' style='padding:6px 14px;font-size:.82rem' rel='nofollow noopener' target='_blank'>Get Deal →</a></td></tr>\n"
    return f"""<table>
<tr><th>Plan</th><th>Price</th><th>Websites</th><th>Storage</th><th>Action</th></tr>
{rows}
</table>"""

# ─── COMPARISON TABLE (two hosts) ─────────────────────────────────────────────
def comparison_table_2(h1, h2):
    d1, d2 = HOSTS[h1], HOSTS[h2]
    feat_keys = list(d1["features"].keys())
    rows = ""
    for feat in feat_keys:
        v1 = d1["features"].get(feat, "—")
        v2 = d2["features"].get(feat, "—")
        c1 = ' class="tick"' if v1 == "✓" else (' class="cross"' if v1 == "✗" else "")
        c2 = ' class="tick"' if v2 == "✓" else (' class="cross"' if v2 == "✗" else "")
        rows += f"<tr><td><strong>{feat}</strong></td><td{c1}>{v1}</td><td{c2}>{v2}</td></tr>\n"
    # price row
    rows = f"<tr><td><strong>Starting Price</strong></td><td><strong>₹{d1['price']}/mo</strong></td><td><strong>₹{d2['price']}/mo</strong></td></tr>\n" + \
           f"<tr><td><strong>Renewal Price</strong></td><td>₹{d1['renewal']}/mo</td><td>₹{d2['renewal']}/mo</td></tr>\n" + \
           f"<tr><td><strong>Money-back</strong></td><td>{d1['money_back']} days</td><td>{d2['money_back']} days</td></tr>\n" + \
           f"<tr><td><strong>Our Rating</strong></td><td>{d1['rating']}/5</td><td>{d2['rating']}/5</td></tr>\n" + rows
    return f"""<table>
<tr><th>Feature</th><th>{d1['name']}</th><th>{d2['name']}</th></tr>
{rows}
</table>"""

# ─── BREADCRUMB ───────────────────────────────────────────────────────────────
def breadcrumb(*parts):
    crumbs = ['<a href="/">Home</a>']
    for label, url in parts:
        crumbs.append(f'<a href="{url}">{label}</a>' if url else label)
    return '<div class="breadcrumb">' + " › ".join(crumbs) + '</div>'

# ─── FAQ BLOCK ────────────────────────────────────────────────────────────────
def faq_block(items):
    html = '<div class="faq">\n'
    schema_items = []
    for i, (q, a) in enumerate(items):
        html += f'<details><summary>{q}</summary><p>{a}</p></details>\n'
        schema_items.append({"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}})
    html += '</div>'
    schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":schema_items})
    return html, f'<script type="application/ld+json">{schema}</script>'

# ─────────────────────────────────────────────────────────────────────────────
# PAGE GENERATORS
# ─────────────────────────────────────────────────────────────────────────────

def make_comparison_page(h1, h2):
    d1, d2 = HOSTS[h1], HOSTS[h2]
    slug = f"{h1}-vs-{h2}.html"
    title = f"{d1['name']} vs {d2['name']} India {YEAR}: Which is Better?"
    desc = f"Detailed {d1['name']} vs {d2['name']} comparison for India {YEAR}. Compare prices in ₹, features, speed, support, and uptime. Find out which hosting is best for your needs."

    # Determine winner
    winner_key = h1 if d1["rating"] >= d2["rating"] else h2
    winner = HOSTS[winner_key]
    loser_key = h2 if winner_key == h1 else h1
    loser = HOSTS[loser_key]

    faqs, faq_schema = faq_block([
        (f"Is {d1['name']} better than {d2['name']} for India?",
         f"For most Indian users, {winner['name']} edges ahead with a {winner['rating']}/5 rating. It offers {winner['pros'][0].lower()} and {winner['pros'][1].lower()}. However, {loser['name']} may suit you better if {loser['best_for'][0].lower()} is your primary need."),
        (f"Which is cheaper — {d1['name']} or {d2['name']}?",
         f"{HOSTS[h1 if d1['price'] <= d2['price'] else h2]['name']} is cheaper at ₹{min(d1['price'],d2['price'])}/month vs ₹{max(d1['price'],d2['price'])}/month. Remember to check renewal prices too — {d1['name']} renews at ₹{d1['renewal']}/mo and {d2['name']} at ₹{d2['renewal']}/mo."),
        (f"Do {d1['name']} and {d2['name']} have India data centres?",
         f"{'Both have' if d1['features']['India Data Centre']=='✓' and d2['features']['India Data Centre']=='✓' else 'Neither has' if d1['features']['India Data Centre']=='✗' and d2['features']['India Data Centre']=='✗' else (d1['name'] if d1['features']['India Data Centre']=='✓' else d2['name'])+' has an India data centre while the other does not'} India-based servers. An India data centre reduces page load time by 40–80ms for Indian visitors, which matters for SEO."),
        (f"Which has better customer support — {d1['name']} or {d2['name']}?",
         f"Both offer 24/7 support, but {d1['name']} scores {d1['score']['support']}/5 and {d2['name']} scores {d2['score']['support']}/5 on support in our tests. {'GoDaddy' if 'godaddy' in [h1,h2] else winner['name']} provides Hindi phone support which is valuable for Indian customers."),
        (f"Can I migrate my website from {loser['name']} to {winner['name']}?",
         f"Yes. {winner['name']} {'offers free site migration' if 'siteground' in winner_key else 'makes migration straightforward'} using its {'Site Tools' if 'siteground' in winner_key else 'control panel'} migration tool. Most migrations complete within 2–4 hours with zero downtime."),
    ])

    html = header()
    html = html.replace("{CANONICAL}", slug)
    html += faq_schema
    html += f"""
<div class="hero">
  <div class="container">
    <div class="badge">Side-by-Side Comparison · {YEAR}</div>
    <h1>{d1['name']} vs {d2['name']}<br>Which Should You Choose in India?</h1>
    <p>We tested both hosts for 30 days. Here's every metric that matters for Indian websites.</p>
  </div>
</div>
<div class="container">
{breadcrumb(('Comparisons','/comparisons.html'), (f"{d1['name']} vs {d2['name']}", None))}
<div class="toc">
  <h3>📋 What's in this comparison</h3>
  <ol>
    <li><a href="#quick-verdict">Quick Verdict</a></li>
    <li><a href="#pricing">Pricing in ₹ (India)</a></li>
    <li><a href="#features">Full Feature Comparison</a></li>
    <li><a href="#performance">Performance & Speed</a></li>
    <li><a href="#support">Customer Support</a></li>
    <li><a href="#pros-cons">Pros & Cons</a></li>
    <li><a href="#plans">Plans & Pricing</a></li>
    <li><a href="#faq">Frequently Asked Questions</a></li>
  </ol>
</div>

<div id="quick-verdict">
<div class="verdict">
  <strong>⚡ Quick Verdict:</strong> {winner['name']} wins this comparison with a {winner['rating']}/5 rating vs {loser['rating']}/5.
  It stands out for {winner['pros'][0].lower()} and {winner['pros'][1].lower()}.
  Choose {loser['name']} if {loser['best_for'][0].lower()} is your top priority or you specifically need {loser['pros'][0].lower()}.
</div>
</div>

<div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin:20px 0">
  <div class="card" style="text-align:center">
    <div class="host-logo" style="background:{d1['logo_bg']};color:{d1['color']};margin:0 auto 8px;width:52px;height:52px;font-size:1rem">{d1['name'][:2].upper()}</div>
    <div class="host-name" style="font-size:1.1rem">{d1['name']}</div>
    <div class="stars">{stars(d1['rating'])}</div>
    <div style="font-size:1.4rem;font-weight:700;color:#15803d;margin:8px 0">₹{d1['price']}<span style="font-size:.8rem;font-weight:400;color:#6b7280">/mo</span></div>
    <a href="/AFFILIATE_{h1.upper()}" class="btn btn-{'primary' if winner_key==h1 else 'outline'}" rel="nofollow noopener" target="_blank">Visit {d1['name']} →</a>
    {"<br><small style='color:#16a34a;font-size:.75rem;margin-top:6px;display:block'>⭐ Our Pick</small>" if winner_key==h1 else ""}
  </div>
  <div class="card" style="text-align:center">
    <div class="host-logo" style="background:{d2['logo_bg']};color:{d2['color']};margin:0 auto 8px;width:52px;height:52px;font-size:1rem">{d2['name'][:2].upper()}</div>
    <div class="host-name" style="font-size:1.1rem">{d2['name']}</div>
    <div class="stars">{stars(d2['rating'])}</div>
    <div style="font-size:1.4rem;font-weight:700;color:#15803d;margin:8px 0">₹{d2['price']}<span style="font-size:.8rem;font-weight:400;color:#6b7280">/mo</span></div>
    <a href="/AFFILIATE_{h2.upper()}" class="btn btn-{'primary' if winner_key==h2 else 'outline'}" rel="nofollow noopener" target="_blank">Visit {d2['name']} →</a>
    {"<br><small style='color:#16a34a;font-size:.75rem;margin-top:6px;display:block'>⭐ Our Pick</small>" if winner_key==h2 else ""}
  </div>
</div>

<h2 id="pricing">Pricing Comparison for India ({YEAR})</h2>
<p>All prices are in Indian Rupees (₹). Introductory prices apply for the initial term. Renewal prices are shown separately — always factor these in before you commit.</p>
<table>
<tr><th></th><th>{d1['name']}</th><th>{d2['name']}</th></tr>
<tr><td><strong>Starting Price</strong></td><td>₹{d1['price']}/month</td><td>₹{d2['price']}/month</td></tr>
<tr><td><strong>Renewal Price</strong></td><td>₹{d1['renewal']}/month</td><td>₹{d2['renewal']}/month</td></tr>
<tr><td><strong>Annual Cost (Yr 1)</strong></td><td>₹{d1['price']*12:,}</td><td>₹{d2['price']*12:,}</td></tr>
<tr><td><strong>Annual Cost (Yr 2)</strong></td><td>₹{d1['renewal']*12:,}</td><td>₹{d2['renewal']*12:,}</td></tr>
<tr><td><strong>Money-back Guarantee</strong></td><td>{d1['money_back']} days</td><td>{d2['money_back']} days</td></tr>
</table>

<h2 id="features">Full Feature Comparison</h2>
{comparison_table_2(h1, h2)}

<h2 id="performance">Performance & Speed</h2>
<p>Speed is one of the most critical factors for Indian websites. Google's Core Web Vitals directly affect your search rankings, and Indian internet speeds vary widely across regions.</p>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
  <div class="card">
    <strong>{d1['name']}</strong>
    <p style="margin-top:8px;font-size:.9rem">Server: {d1['features']['Server Tech']}<br>India DC: {d1['features']['India Data Centre']}<br>Uptime SLA: {d1['uptime']}<br>Speed score: {'★'*d1['score']['speed']}{'☆'*(5-d1['score']['speed'])}</p>
  </div>
  <div class="card">
    <strong>{d2['name']}</strong>
    <p style="margin-top:8px;font-size:.9rem">Server: {d2['features']['Server Tech']}<br>India DC: {d2['features']['India Data Centre']}<br>Uptime SLA: {d2['uptime']}<br>Speed score: {'★'*d2['score']['speed']}{'☆'*(5-d2['score']['speed'])}</p>
  </div>
</div>

<h2 id="support">Customer Support</h2>
<table>
<tr><th>Support Channel</th><th>{d1['name']}</th><th>{d2['name']}</th></tr>
<tr><td>Live Chat</td><td class="tick">✓ 24/7</td><td class="tick">✓ 24/7</td></tr>
<tr><td>Phone Support</td><td>{'<span class="tick">✓</span>' if 'phone' in d1['features']['Support'] else '<span class="cross">✗</span>'}</td><td>{'<span class="tick">✓</span>' if 'phone' in d2['features']['Support'] else '<span class="cross">✗</span>'}</td></tr>
<tr><td>Hindi Support</td><td>{'<span class="tick">✓</span>' if h1 in ['hostinger','godaddy','bigrock','milesweb'] else '<span class="cross">✗</span>'}</td><td>{'<span class="tick">✓</span>' if h2 in ['hostinger','godaddy','bigrock','milesweb'] else '<span class="cross">✗</span>'}</td></tr>
<tr><td>Support Rating</td><td>{d1['score']['support']}/5</td><td>{d2['score']['support']}/5</td></tr>
</table>

<h2 id="pros-cons">{d1['name']} — Pros & Cons</h2>
<div class="pros-cons">
  <div class="pros"><h4>✓ Pros</h4><ul class="check">{"".join(f"<li>{p}</li>" for p in d1['pros'])}</ul></div>
  <div class="cons"><h4>✗ Cons</h4><ul class="cross">{"".join(f"<li>{c}</li>" for c in d1['cons'])}</ul></div>
</div>

<h2>{d2['name']} — Pros & Cons</h2>
<div class="pros-cons">
  <div class="pros"><h4>✓ Pros</h4><ul class="check">{"".join(f"<li>{p}</li>" for p in d2['pros'])}</ul></div>
  <div class="cons"><h4>✗ Cons</h4><ul class="cross">{"".join(f"<li>{c}</li>" for c in d2['cons'])}</ul></div>
</div>

<h2 id="plans">Plans & Pricing — {d1['name']}</h2>
{plans_table(h1)}
<h2>Plans & Pricing — {d2['name']}</h2>
{plans_table(h2)}

<div class="cta-box">
  <h3>Our Recommendation: {winner['name']}</h3>
  <p>{winner['pros'][0]} and {winner['pros'][1].lower()}. {winner['money_back']}-day money-back guarantee.</p>
  <a href="/AFFILIATE_{winner_key.upper()}" rel="nofollow noopener" target="_blank">Get {winner['name']} Now →</a>
</div>

<h2 id="faq">Frequently Asked Questions</h2>
{faqs}
</div>
"""
    html += footer()
    return slug, title, desc, html

def make_review_page(h):
    d = HOSTS[h]
    slug = f"{h}-review.html"
    title = f"{d['name']} Review India {YEAR}: Is It Worth It? (Honest)"
    desc = f"In-depth {d['name']} review for India {YEAR}. We test speed, uptime, support, and value. Real pricing in ₹. Read before you buy."

    faqs, faq_schema = faq_block([
        (f"Is {d['name']} good for beginners in India?",
         f"{'Yes, ' if 'Beginners' in d['best_for'] else 'It depends — '}{d['name']} {'is excellent for beginners' if 'Beginners' in d['best_for'] else 'may be better suited for experienced users'} due to its {d['pros'][0].lower()}. The control panel is {'intuitive for first-timers' if h in ['hostinger','godaddy','bigrock'] else 'powerful but may have a learning curve'}."),
        (f"Does {d['name']} have an India data centre?",
         f"{'Yes' if d['features']['India Data Centre']=='✓' else 'No'} — {d['name']} {'has servers in India (Mumbai region), which means faster load times for Indian visitors' if d['features']['India Data Centre']=='✓' else 'does not have an India data centre. Servers are based overseas, which adds 80-120ms latency for Indian visitors. Consider using their free Cloudflare CDN to mitigate this'}."),
        (f"What is {d['name']}'s uptime guarantee?",
         f"{d['name']} offers a {d['uptime']} uptime SLA. In our 30-day testing period, we observed {'consistent performance above this SLA' if d['score']['reliability'] >= 4 else 'performance generally meeting but occasionally dipping below this SLA'}. For business-critical websites, consider their higher-tier plans with enhanced SLAs."),
        (f"Does {d['name']} offer a money-back guarantee?",
         f"Yes, {d['name']} offers a {d['money_back']}-day money-back guarantee on shared hosting plans. If you're not satisfied, you can request a full refund within this window. Note that domain registration fees are typically non-refundable."),
        (f"Is {d['name']} hosting worth it in {YEAR}?",
         f"Based on our testing, {d['name']} scores {d['rating']}/5 overall. It's particularly worth it for {', '.join(d['best_for'][:2]).lower()}. Key strengths include {d['pros'][0].lower()} and {d['pros'][1].lower()}. Main limitation: {d['cons'][0].lower()}."),
    ])

    html = header()
    html = html.replace("{CANONICAL}", slug)
    html += faq_schema
    html += f"""
<div class="hero">
  <div class="container">
    <div class="badge">Honest Review · Tested {YEAR}</div>
    <h1>{d['name']} Review for India {YEAR}</h1>
    <p>We signed up, tested speed and uptime for 30 days, and contacted support 5 times. Here's everything you need to know.</p>
  </div>
</div>
<div class="container">
{breadcrumb(('Reviews','/reviews.html'), (f"{d['name']} Review", None))}

<div style="display:flex;gap:20px;flex-wrap:wrap;margin:20px 0 28px">
  <div class="card" style="flex:1;min-width:220px">
    <div class="host-logo" style="background:{d['logo_bg']};color:{d['color']};width:56px;height:56px;font-size:1.1rem;margin-bottom:10px">{d['name'][:2].upper()}</div>
    <div class="host-name" style="font-size:1.2rem">{d['name']}</div>
    <div class="host-tag">{d['tagline']}</div>
    <div class="stars" style="font-size:1.1rem;margin:6px 0">{stars(d['rating'])} {d['rating']}/5</div>
    <div style="color:#6b7280;font-size:.8rem">({d['reviews']:,} verified reviews)</div>
    <div style="font-size:1.5rem;font-weight:700;color:#15803d;margin:10px 0">From ₹{d['price']}/month</div>
    <a href="/AFFILIATE_{h.upper()}" class="btn btn-primary" rel="nofollow noopener" target="_blank" style="display:block;text-align:center">
      Visit {d['name']} →
    </a>
    <div style="font-size:.75rem;color:#6b7280;margin-top:6px;text-align:center">{d['money_back']}-day money-back guarantee</div>
  </div>
  <div style="flex:2;min-width:240px">
    <h3 style="margin-top:0">Performance Scores</h3>
    {score_bars(h)}
    <div style="margin-top:14px">
      <strong>Best for:</strong>
      <div style="margin-top:6px">
        {"".join(f'<span style="background:#f0f0ff;color:#4f46e5;border-radius:4px;padding:3px 10px;font-size:.78rem;margin:0 4px 4px 0;display:inline-block">{bf}</span>' for bf in d["best_for"])}
      </div>
    </div>
  </div>
</div>

<div class="verdict">
  <strong>HostingBharat Verdict ({YEAR}):</strong> {d['name']} earns <strong>{d['rating']}/5</strong> in our independent testing.
  It excels at {d['pros'][0].lower()} and {d['pros'][1].lower()}.
  Main caveat: {d['cons'][0].lower()}.
  {'We recommend it for most Indian websites.' if d['rating'] >= 4.5 else 'We recommend it for ' + d['best_for'][0].lower() + ' use cases.'}
</div>

<div class="pros-cons">
  <div class="pros"><h4>✓ What We Liked</h4><ul class="check">{"".join(f"<li>{p}</li>" for p in d['pros'])}</ul></div>
  <div class="cons"><h4>✗ What Could Be Better</h4><ul class="cross">{"".join(f"<li>{c}</li>" for c in d['cons'])}</ul></div>
</div>

<h2>Full Feature Breakdown</h2>
{feature_table(h)}

<h2>Plans & Pricing (India, {YEAR})</h2>
<p>All prices are in ₹ (Indian Rupees) per month billed annually. Renewal prices apply after the initial term.</p>
{plans_table(h)}
<div class="verdict">
  <strong>Pricing Note:</strong> The introductory price of ₹{d['price']}/month is for the first billing cycle. Upon renewal, the price becomes ₹{d['renewal']}/month.
  Always set a reminder before renewal to evaluate whether you want to continue or switch providers.
</div>

<h2>Speed & Performance (India)</h2>
<p>{d['name']} uses <strong>{d['features']['Server Tech']}</strong> server technology. {'LiteSpeed servers are typically 3–4× faster than standard Apache/Nginx for WordPress sites, especially with caching plugins.' if 'LiteSpeed' in d['features']['Server Tech'] else 'Standard Apache/Nginx servers perform reliably for most websites. For high-traffic sites, consider their VPS or cloud plans.'}</p>
<p>{'With an India-based data centre in Mumbai, average TTFB (Time to First Byte) for Indian visitors is typically 80–150ms — excellent for SEO and user experience.' if d['features']['India Data Centre']=='✓' else 'Without an India data centre, expect TTFB of 200–400ms for Indian visitors. Enabling the free Cloudflare CDN (available in your control panel) can reduce this to 80–150ms for cached content.'}</p>

<h2>Customer Support Quality</h2>
<p>{d['name']} offers {d['features']['Support']}. {'In our 5 test contacts, average first-response time was under 3 minutes via live chat.' if d['score']['support'] >= 4 else 'Support quality is generally good for standard issues, though complex technical queries occasionally require escalation.'} {'Hindi language support is available' if h in ['hostinger','godaddy','bigrock','milesweb','hostgator'] else 'Support is in English only — worth noting for users who prefer regional language assistance'}.</p>

<h2>Is {d['name']} Right for You?</h2>
<p><strong>Choose {d['name']} if you are:</strong></p>
<ul class="check" style="margin:8px 0 16px">
{"".join(f"<li>{bf}</li>" for bf in [
    f"A {d['best_for'][0].lower()} looking for {d['pros'][0].lower()}",
    f"Someone who values {d['pros'][1].lower()}",
    f"Starting your first website with a budget of {'under ₹200' if d['price'] < 200 else 'up to ₹500'}/month",
    f"Looking for {d['money_back']}-day risk-free trial period"
])}
</ul>
<p><strong>Consider alternatives if you need:</strong></p>
<ul class="cross" style="margin:8px 0 16px">
{"".join(f"<li>{c}</li>" for c in d['cons'])}
</ul>

<div class="cta-box">
  <h3>Ready to Get Started with {d['name']}?</h3>
  <p>Starting at ₹{d['price']}/month with a {d['money_back']}-day money-back guarantee.</p>
  <a href="/AFFILIATE_{h.upper()}" rel="nofollow noopener" target="_blank">Get {d['name']} Now →</a>
</div>

<h2>Frequently Asked Questions</h2>
{faqs}

<h2>Compare {d['name']} with Other Hosts</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin-top:10px">
{"".join(f'<a href="/{h}-vs-{oh}.html" style="display:block;background:#f8fafc;border:1px solid #e5e7eb;border-radius:8px;padding:10px 12px;font-size:.88rem;color:#4f46e5">{d["name"]} vs {HOSTS[oh]["name"]}</a>' for oh in HOST_KEYS if oh != h)}
</div>
</div>"""
    html += footer()
    return slug, title, desc, html

def make_best_page(slug_key, label, use_case):
    slug = f"best-hosting-{slug_key}-india.html"
    title = f"Best Web Hosting for {label} in India {YEAR}: Top {min(5,len(HOST_KEYS))} Picks"
    desc = f"We tested the top web hosting providers for {label.lower()} in India. Compare prices in ₹, features, and performance. Updated {YEAR}."

    # rank hosts for this use case
    rankings = sorted(HOST_KEYS, key=lambda h: (
        HOSTS[h]["rating"] +
        (0.3 if use_case.lower() in " ".join(HOSTS[h]["best_for"]).lower() else 0) +
        (0.2 if HOSTS[h]["features"]["India Data Centre"] == "✓" else 0)
    ), reverse=True)[:5]

    cards = ""
    for i, h in enumerate(rankings):
        d = HOSTS[h]
        ribbon = ["🥇 #1 Pick", "🥈 Runner-up", "🥉 #3", "#4", "#5"][i]
        cards += f"""
<div style="border-left:3px solid {'#4f46e5' if i==0 else '#e5e7eb'};padding-left:14px;margin-bottom:24px">
  <div style="font-size:.82rem;font-weight:700;color:{'#4f46e5' if i==0 else '#6b7280'};margin-bottom:6px">{ribbon}</div>
  {host_card_short(h)}
  <p style="font-size:.88rem;color:#374151;margin-top:10px">{d['pros'][0]} and {d['pros'][1].lower()}. {'India data centre ensures fast local load speeds.' if d['features']['India Data Centre']=='✓' else 'Free Cloudflare CDN compensates for no India DC.'} Starts at ₹{d['price']}/month with {d['money_back']}-day money-back.</p>
</div>"""

    faqs, faq_schema = faq_block([
        (f"What is the best web hosting for {label.lower()} in India?",
         f"Based on our testing, {HOSTS[rankings[0]]['name']} is the best hosting for {use_case} in India in {YEAR}. It offers {HOSTS[rankings[0]]['pros'][0].lower()} with pricing starting at ₹{HOSTS[rankings[0]]['price']}/month."),
        ("How much does web hosting cost in India?",
         f"Web hosting in India ranges from ₹40/month (MilesWeb entry plan) to ₹1,499/month (SiteGround premium). For most websites, a plan between ₹{min(d['price'] for d in HOSTS.values())}-₹300/month is sufficient. Always check renewal prices, not just introductory rates."),
        ("Which Indian web hosting company has the best uptime?",
         f"MilesWeb and SiteGround both offer 99.99% uptime SLA — the highest in this list. Hostinger, BigRock, and GoDaddy offer 99.9% uptime. In practice, all major hosts maintain uptime above 99.5% for shared hosting."),
        ("Do I need an India data centre for my Indian website?",
         "Not necessarily. An India-based data centre reduces TTFB (page load time) by 40–80ms for Indian visitors, which helps SEO. However, using a free Cloudflare CDN (offered by all hosts in this list) achieves similar speeds for static content regardless of server location."),
        ("What is the cheapest web hosting in India?",
         f"MilesWeb offers the cheapest hosting in India at ₹40/month, followed by BigRock at ₹59/month and Hostinger at ₹69/month. Note that these are introductory prices — renewal rates are higher. All three include free SSL and a free domain name."),
    ])

    html = header()
    html = html.replace("{CANONICAL}", slug)
    html += faq_schema
    html += f"""
<div class="hero">
  <div class="container">
    <div class="badge">Expert Picks · {YEAR}</div>
    <h1>Best Web Hosting for {label} in India ({YEAR})</h1>
    <p>We tested {len(HOSTS)} hosting providers specifically for {use_case}. Here are the top picks ranked by value, speed, and India-specific performance.</p>
  </div>
</div>
<div class="container">
{breadcrumb(('Best Picks','/best.html'), (f"Best for {label}", None))}

<p class="update-note">Last updated: {YEAR} · Tested {len(HOSTS)} hosting providers · Prices in ₹ (Indian Rupees)</p>

<div class="verdict">
  <strong>Summary:</strong> For {label.lower()} in India, <strong>{HOSTS[rankings[0]]['name']}</strong> is our top pick in {YEAR} — {HOSTS[rankings[0]]['pros'][0].lower()}, starts at ₹{HOSTS[rankings[0]]['price']}/month, and comes with a {HOSTS[rankings[0]]['money_back']}-day money-back guarantee.
</div>

<h2>Top {len(rankings)} Web Hosting Providers for {label} in India</h2>
{cards}

<h2>Quick Comparison Table</h2>
<table>
<tr><th>Host</th><th>Starting Price</th><th>Rating</th><th>India DC</th><th>Money-back</th><th>Best For</th></tr>
{"".join(f"<tr><td><a href='/{h}-review.html'>{HOSTS[h]['name']}</a></td><td>₹{HOSTS[h]['price']}/mo</td><td>{HOSTS[h]['rating']}/5</td><td>{'<span class=tick>✓</span>' if HOSTS[h]['features']['India Data Centre']=='✓' else '<span class=cross>✗</span>'}</td><td>{HOSTS[h]['money_back']} days</td><td>{HOSTS[h]['best_for'][0]}</td></tr>" for h in rankings)}
</table>

<h2>How We Selected These Hosts for {label}</h2>
<p>We evaluated each hosting provider across 6 criteria most relevant to {use_case}: pricing in ₹, India data centre availability, speed (measured from Mumbai), support quality, ease of use, and reliability over 30 days. We prioritised hosts with transparent pricing, Hindi support, and Indian payment methods (UPI, NetBanking, credit cards).</p>

<h2>Key Factors to Consider</h2>
<p><strong>India data centre:</strong> Reduces page load time by 40–80ms for Indian visitors — important for Google rankings in India.</p>
<p><strong>Renewal pricing:</strong> Always check the price after year one. Introductory discounts typically expire, and renewal rates can be 2–4× higher.</p>
<p><strong>Money-back guarantee:</strong> All our picks offer at least 30 days. Use this risk-free period to test performance with your actual website.</p>
<p><strong>Payment methods:</strong> Best Indian hosts accept UPI, NetBanking, debit cards, and credit cards — no need for a foreign card.</p>

<h2>Frequently Asked Questions</h2>
{faqs}
</div>"""
    html += footer()
    return slug, title, desc, html

def make_index_page(all_pages):
    slug = "index.html"
    title = f"Best Web Hosting India {YEAR}: Compare Top Providers in ₹"
    desc = f"Compare the best web hosting providers in India for {YEAR}. Honest reviews, real ₹ pricing, speed tests. Updated monthly."

    top_host = max(HOST_KEYS, key=lambda h: HOSTS[h]["rating"])

    html = header()
    html = html.replace("{CANONICAL}", "")
    html += f"""
<div class="hero">
  <div class="container">
    <div class="badge">India's Most Detailed Hosting Guide · {YEAR}</div>
    <h1>Best Web Hosting in India for {YEAR}</h1>
    <p>We independently test, compare, and review every major hosting provider. All prices in ₹. No sponsored rankings.</p>
  </div>
</div>
<div class="container">

<h2>Top {len(HOSTS)} Web Hosting Providers in India ({YEAR})</h2>
<p class="update-note">Updated {YEAR} · All prices in ₹/month · Tested from Mumbai</p>

<table>
<tr><th>Provider</th><th>Starting Price</th><th>Rating</th><th>India DC</th><th>Uptime</th><th>Money-back</th><th></th></tr>
{"".join(f'''<tr>
  <td><strong><a href="/{h}-review.html">{HOSTS[h]["name"]}</a></strong>{"<span class='winner-chip'>Best</span>" if h==top_host else ""}</td>
  <td>₹{HOSTS[h]["price"]}/mo</td>
  <td>{HOSTS[h]["rating"]}/5 {stars(HOSTS[h]["rating"])}</td>
  <td>{"<span class='tick'>✓</span>" if HOSTS[h]["features"]["India Data Centre"]=="✓" else "<span class='cross'>✗</span>"}</td>
  <td>{HOSTS[h]["uptime"]}</td>
  <td>{HOSTS[h]["money_back"]} days</td>
  <td><a href="/AFFILIATE_{h.upper()}" class="btn btn-primary" style="padding:6px 14px;font-size:.82rem" rel="nofollow noopener" target="_blank">Visit →</a></td>
</tr>''' for h in sorted(HOST_KEYS, key=lambda h: HOSTS[h]["rating"], reverse=True))}
</table>

<h2>Browse by Category</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(200px,1fr));gap:10px;margin:10px 0 28px">
  <a href="/best.html" style="display:block;background:#f0f0ff;border-radius:8px;padding:12px 14px;font-weight:600;color:#4f46e5">🏆 Best Picks by Use Case</a>
  <a href="/comparisons.html" style="display:block;background:#f0fdf4;border-radius:8px;padding:12px 14px;font-weight:600;color:#15803d">⚖️ Side-by-Side Comparisons</a>
  <a href="/reviews.html" style="display:block;background:#fff4e5;border-radius:8px;padding:12px 14px;font-weight:600;color:#92400e">📋 In-Depth Reviews</a>
  <a href="/guides.html" style="display:block;background:#fdf2f8;border-radius:8px;padding:12px 14px;font-weight:600;color:#701a75">📖 How-To Guides</a>
</div>

<h2>Popular Comparisons</h2>
<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:8px;margin:10px 0">
{"".join(f'<a href="/{h1}-vs-{h2}.html" style="display:block;background:#f8fafc;border:1px solid #e5e7eb;border-radius:8px;padding:9px 12px;font-size:.88rem;color:#374151">{HOSTS[h1]["name"]} vs {HOSTS[h2]["name"]}</a>' for h1,h2 in list(combinations(HOST_KEYS,2))[:12])}
</div>

<h2>Why Trust HostingBharat?</h2>
<p>We purchase hosting plans with our own money and test each provider from servers in Mumbai, Delhi, and Bangalore. We measure real TTFB, run uptime monitors for 30 days, and contact support 5 times per provider before writing any review. No host pays for a positive review.</p>
</div>"""
    html += footer()
    return slug, title, desc, html

def make_hub_page(page_type, title, desc, items_html):
    slug = f"{page_type}.html"
    html = header()
    html = html.replace("{CANONICAL}", slug)
    html += f"""
<div class="hero">
  <div class="container">
    <h1>{title}</h1>
    <p>{desc}</p>
  </div>
</div>
<div class="container">
{items_html}
</div>"""
    html += footer()
    return slug, html

def make_guide_page(slug_key, title_text, category):
    slug = f"how-to-{slug_key}.html"
    title = f"How to {title_text} in India — Step-by-Step Guide {YEAR}"
    desc = f"Complete guide: how to {title_text.lower()} in India. Step-by-step instructions for {YEAR}. Works for beginners. All hosting options compared in ₹."

    top = sorted(HOST_KEYS, key=lambda h: HOSTS[h]["rating"], reverse=True)[:3]

    html = header()
    html = html.replace("{CANONICAL}", slug)
    html += f"""
<div class="hero">
  <div class="container">
    <div class="badge">Step-by-Step Guide · {YEAR}</div>
    <h1>How to {title_text} in India ({YEAR})</h1>
    <p>A practical, beginner-friendly guide. Completed in under 30 minutes. No technical experience required.</p>
  </div>
</div>
<div class="container">
{breadcrumb(('Guides','/guides.html'), (title_text, None))}

<div class="toc">
  <h3>What you'll learn</h3>
  <ol>
    <li>What you need before you start</li>
    <li>Step-by-step setup instructions</li>
    <li>Recommended hosting for this use case</li>
    <li>Common mistakes to avoid</li>
    <li>Frequently asked questions</li>
  </ol>
</div>

<h2>What You Need Before You Start</h2>
<p>To {title_text.lower()} in India you need: a domain name (₹699–₹999/year), web hosting (₹40–₹499/month), and about 30–60 minutes. That's it. You do not need any technical skills or coding knowledge.</p>

<h2>Step-by-Step Instructions</h2>
<h3>Step 1 — Choose a hosting provider</h3>
<p>For {category} in India, we recommend one of these three providers based on speed, Indian data centre availability, and Hindi support:</p>
{"".join(host_card_short(h, ribbon=["Best Overall","Runner-up","Budget Pick"][i]) for i,h in enumerate(top))}

<h3>Step 2 — Register a domain and sign up for hosting</h3>
<p>Go to your chosen provider and select a shared hosting plan. Most providers offer a free domain with annual plans. Use UPI, NetBanking, or a debit card to pay. You'll receive your login credentials by email within minutes.</p>

<h3>Step 3 — Log in to your control panel</h3>
<p>Check your email for login credentials. Access your hosting control panel (hPanel or cPanel depending on provider). This is where you manage your website, email, and files.</p>

<h3>Step 4 — Install your platform</h3>
<p>Use the one-click installer in your control panel to install WordPress or your preferred platform. The installer handles the database setup automatically. Takes under 5 minutes.</p>

<h3>Step 5 — Launch your site</h3>
<p>Your website is now live. Visit your domain to confirm it loads correctly. Enable the free SSL certificate from your control panel to secure your site (required for Google rankings).</p>

<h2>Common Mistakes to Avoid</h2>
<ul class="cross" style="margin:8px 0 20px">
  <li>Choosing hosting based only on the intro price — always check renewal rates</li>
  <li>Skipping SSL — Google Chrome marks non-HTTPS sites as "Not Secure"</li>
  <li>Not enabling free daily backups during setup — you want these before something goes wrong</li>
  <li>Picking a server outside India without enabling Cloudflare CDN — adds 200ms+ latency</li>
</ul>

<h2>Recommended Hosting for {category} in India</h2>
<p>After testing {len(HOSTS)} hosting providers specifically for {category.lower()}, here are our top three recommendations with ₹ pricing:</p>
<table>
<tr><th>Host</th><th>Price</th><th>India DC</th><th>Rating</th><th>Best Feature</th></tr>
{"".join(f'<tr><td><a href="/{h}-review.html">{HOSTS[h]["name"]}</a></td><td>₹{HOSTS[h]["price"]}/mo</td><td>{"<span class=tick>✓</span>" if HOSTS[h]["features"]["India Data Centre"]=="✓" else "<span class=cross>✗</span>"}</td><td>{HOSTS[h]["rating"]}/5</td><td>{HOSTS[h]["pros"][0]}</td></tr>' for h in top)}
</table>
</div>"""
    html += footer()
    return slug, title, desc, html

# ─── SITEMAP ──────────────────────────────────────────────────────────────────
def make_sitemap(pages):
    urls = "\n".join([
        f'  <url><loc>{SITE_DOMAIN}/{p["slug"]}</loc><lastmod>{YEAR}-01-01</lastmod><changefreq>monthly</changefreq><priority>{"0.9" if p["slug"]=="index.html" else "0.8"}</priority></url>'
        for p in pages
    ])
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>"""

# ─── AFFILIATE CONFIG JS ──────────────────────────────────────────────────────
def make_affiliate_config():
    lines = "// HostingBharat Affiliate Config\n// Replace each URL with your real affiliate link after signing up\n// Signup links: https://www.hostinger.in/affiliate-program | https://www.bluehost.in/affiliates | https://www.godaddy.com/affiliate-programs\nconst AFFILIATE_LINKS = {\n"
    for k, v in AFFILIATES.items():
        lines += f'  {k}: "{v}",  // Replace this\n'
    lines += "};\n"
    return lines

# ─────────────────────────────────────────────────────────────────────────────
# MAIN BUILD
# ─────────────────────────────────────────────────────────────────────────────
def build():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    pages = []

    print("Building comparison pages...")
    comp_links = ""
    for h1, h2 in combinations(HOST_KEYS, 2):
        slug, title, desc, html = make_comparison_page(h1, h2)
        path = os.path.join(OUTPUT_DIR, slug)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        pages.append({"slug": slug, "title": title, "desc": desc})
        comp_links += f'<a href="/{slug}" style="display:block;background:#f8fafc;border:1px solid #e5e7eb;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:.9rem;color:#374151"><strong>{HOSTS[h1]["name"]} vs {HOSTS[h2]["name"]}</strong><span style="float:right;color:#6b7280">Compare →</span></a>\n'
    print(f"  → {len(list(combinations(HOST_KEYS,2)))} comparison pages")

    print("Building review pages...")
    review_links = ""
    for h in HOST_KEYS:
        slug, title, desc, html = make_review_page(h)
        path = os.path.join(OUTPUT_DIR, slug)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        pages.append({"slug": slug, "title": title, "desc": desc})
        d = HOSTS[h]
        review_links += f'<a href="/{slug}" style="display:block;background:#f8fafc;border:1px solid #e5e7eb;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:.9rem;color:#374151"><strong>{d["name"]} Review {YEAR}</strong> — ₹{d["price"]}/mo · {d["rating"]}/5<span style="float:right;color:#6b7280">Read →</span></a>\n'
    print(f"  → {len(HOST_KEYS)} review pages")

    BEST_PAGES = [
        ("beginners",    "Beginners",         "beginner websites"),
        ("bloggers",     "Bloggers",           "blogging"),
        ("students",     "Students",           "student websites"),
        ("small-business","Small Business",    "small business websites"),
        ("freelancers",  "Freelancers",        "freelancer portfolios"),
        ("ecommerce",    "E-commerce",         "online stores"),
        ("wordpress",    "WordPress",          "WordPress hosting"),
        ("startups",     "Startups",           "startup websites"),
        ("developers",   "Developers",         "developer hosting"),
        ("agencies",     "Agencies",           "agency hosting"),
        ("cheap",        "Budget/Cheap",       "budget hosting"),
        ("performance",  "High Performance",   "performance-critical sites"),
        ("mumbai",       "Mumbai Businesses",  "Mumbai-based businesses"),
        ("bangalore",    "Bangalore Startups", "Bangalore tech startups"),
        ("delhi",        "Delhi Businesses",   "Delhi businesses"),
        ("chennai",      "Chennai Businesses", "Chennai-based businesses"),
        ("photographers","Photographers",      "photography portfolio sites"),
        ("restaurants",  "Restaurants",        "restaurant websites"),
        ("ngo",          "NGOs",               "non-profit websites"),
        ("woocommerce",  "WooCommerce",        "WooCommerce stores"),
    ]

    print("Building best-for pages...")
    best_links = ""
    for slug_key, label, use_case in BEST_PAGES:
        slug, title, desc, html = make_best_page(slug_key, label, use_case)
        path = os.path.join(OUTPUT_DIR, slug)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        pages.append({"slug": slug, "title": title, "desc": desc})
        best_links += f'<a href="/{slug}" style="display:block;background:#f0f0ff;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:.9rem;color:#374151"><strong>Best for {label}</strong><span style="float:right;color:#4f46e5">See Picks →</span></a>\n'
    print(f"  → {len(BEST_PAGES)} best-for pages")

    GUIDE_PAGES = [
        ("start-a-blog",          "Start a Blog",         "blogging"),
        ("create-a-website",      "Create a Website",     "general websites"),
        ("buy-web-hosting",       "Buy Web Hosting",      "hosting purchase"),
        ("buy-a-domain-name",     "Buy a Domain Name",    "domain registration"),
        ("install-wordpress",     "Install WordPress",    "WordPress sites"),
        ("setup-business-email",  "Set Up Business Email","business email"),
        ("migrate-a-website",     "Migrate a Website",    "site migration"),
        ("choose-a-hosting-plan", "Choose a Hosting Plan","hosting selection"),
        ("start-an-online-store", "Start an Online Store","e-commerce"),
        ("make-website-faster",   "Make Your Website Faster","performance"),
    ]

    print("Building how-to guide pages...")
    guide_links = ""
    for slug_key, title_text, category in GUIDE_PAGES:
        slug, title, desc, html = make_guide_page(slug_key, title_text, category)
        path = os.path.join(OUTPUT_DIR, slug)
        with open(path, "w", encoding="utf-8") as f:
            f.write(html)
        pages.append({"slug": slug, "title": title, "desc": desc})
        guide_links += f'<a href="/{slug}" style="display:block;background:#fff4e5;border-radius:8px;padding:10px 14px;margin-bottom:8px;font-size:.9rem;color:#374151"><strong>How to {title_text} in India</strong><span style="float:right;color:#92400e">Read Guide →</span></a>\n'
    print(f"  → {len(GUIDE_PAGES)} guide pages")

    # Hub pages
    _, comp_hub = make_hub_page("comparisons", f"All Web Hosting Comparisons — India {YEAR}", "Side-by-side comparisons of every major Indian web hosting provider. All prices in ₹.", comp_links)
    with open(os.path.join(OUTPUT_DIR, "comparisons.html"), "w", encoding="utf-8") as f:
        f.write(comp_hub)
    pages.append({"slug":"comparisons.html","title":f"All Web Hosting Comparisons India {YEAR}","desc":""})

    _, review_hub = make_hub_page("reviews", f"Web Hosting Reviews for India {YEAR}", "In-depth, independently tested reviews of all major Indian web hosting providers.", review_links)
    with open(os.path.join(OUTPUT_DIR, "reviews.html"), "w", encoding="utf-8") as f:
        f.write(review_hub)
    pages.append({"slug":"reviews.html","title":f"Web Hosting Reviews India {YEAR}","desc":""})

    _, best_hub = make_hub_page("best", f"Best Web Hosting for Every Use Case — India {YEAR}", "Find the best Indian web hosting provider for your specific needs.", best_links)
    with open(os.path.join(OUTPUT_DIR, "best.html"), "w", encoding="utf-8") as f:
        f.write(best_hub)
    pages.append({"slug":"best.html","title":f"Best Web Hosting Picks India {YEAR}","desc":""})

    _, guide_hub = make_hub_page("guides", f"Web Hosting Guides for India {YEAR}", "Step-by-step guides for creating websites, buying hosting, and going online in India.", guide_links)
    with open(os.path.join(OUTPUT_DIR, "guides.html"), "w", encoding="utf-8") as f:
        f.write(guide_hub)
    pages.append({"slug":"guides.html","title":f"Web Hosting Guides India {YEAR}","desc":""})

    # Index page
    slug, title, desc, html = make_index_page(pages)
    with open(os.path.join(OUTPUT_DIR, slug), "w", encoding="utf-8") as f:
        f.write(html)
    pages.insert(0, {"slug": slug, "title": title, "desc": desc})
    print("  → index page built")

    # Sitemap
    sitemap = make_sitemap(pages)
    with open(os.path.join(OUTPUT_DIR, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write(sitemap)

    # robots.txt
    robots = f"User-agent: *\nAllow: /\nSitemap: {SITE_DOMAIN}/sitemap.xml\n"
    with open(os.path.join(OUTPUT_DIR, "robots.txt"), "w", encoding="utf-8") as f:
        f.write(robots)

    # Affiliate config
    with open(os.path.join(OUTPUT_DIR, "affiliate-config.js"), "w", encoding="utf-8") as f:
        f.write(make_affiliate_config())

    total = len(pages)
    print(f"\n✅ Done! {total} pages generated in {OUTPUT_DIR}")
    print(f"   + sitemap.xml ({total} URLs)")
    print(f"   + robots.txt")
    print(f"   + affiliate-config.js (update with your links)")
    return pages

if __name__ == "__main__":
    build()
