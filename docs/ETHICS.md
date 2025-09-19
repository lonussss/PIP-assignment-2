 Ethics and Legal Analysis of Web Scraping NYU Events

This document explores the legal, operational, and ethical implications of scraping data from the NYU Events Calendar, as well as the framework guiding our team’s approach.

---

## ⚖️ 1. Legal Analysis

**U.S. Case Law**  
- *hiQ Labs, Inc. v. LinkedIn Corp.*, 938 F.3d 985 (9th Cir. 2019): The Ninth Circuit ruled that scraping publicly available data is **not a violation** of the Computer Fraud and Abuse Act (CFAA), provided the scraper does not bypass authentication barriers.  
- *Van Buren v. United States*, 593 U.S. ___ (2021): Clarified CFAA scope — “exceeding authorized access” applies only when accessing parts of a system one is not permitted to access. Public pages are generally fair game.  
- *EF Cultural Travel BV v. Zefer Corp.*, 318 F.3d 58 (1st Cir. 2003): Found that scraping could still be challenged under **contract law** (e.g., violating Terms of Service).  

**NYU Events Context**  
- The events posted at [events.nyu.edu](https://events.nyu.edu/) are public-facing.  
- Scraping does **not require login**, bypass security, or access private systems.  

**Conclusion:**  
Our scraping activities are legally safer because we target **public information** without authentication bypass, but we remain mindful of Terms of Service and rate limiting.

---

## ⚙️ 2. Impact on Website Operations

Potential impacts of scraping include:
- **Server load:** Excessive scraping could generate unnecessary traffic.  
- **Rate limiting / bans:** Aggressive requests could trigger anti-bot measures.  
- **Content integrity:** Automated scraping does not alter site content but could unintentionally distort context if data is misused.  

**Mitigation strategies:**
- Implement polite scraping: delays between requests, caching results.  
- 15 second limit per time scraping
- Limit scraping frequency (e.g., once daily).  


---
## 🔒 3. Privacy Considerations

- **Personal data:** NYU Events typically lists event titles, times, and locations. These are organizational details, not personal identifiers.  
- **Risk:** If individual speakers or organizers are listed, this may count as personal data under privacy frameworks (e.g., GDPR Article 4(1)).  
- **Safeguards:**  
  - Do not scrape or redistribute personal contact information.  
  - Avoid combining event data with third-party datasets to infer private details.  
  - Store data securely in JSON/CSV for limited use cases (academic, research).  

---

## 🧭 4. Ethical Framework

Our team’s ethical principles:
1. **Transparency** → Document AI involvement and scraping practices (see `AI_USAGE.md`).  
2. **Proportionality** → Collect only necessary event data (title, date, location, URL).  
3. **Respect for Stakeholders** → Avoid harm to NYU servers or misuse of scraped content.  
4. **Accountability** → Validate and clean data to prevent spreading inaccurate event information.  
5. **Openness** → Share results in formats that enhance access and inclusion (CSV/JSON).  

---

## 🔄 5. Alternative Approaches Considered

- **Official API** → No documented public API for NYU Events was found. If available, this would be preferable for efficiency and compliance.  
- **Manual export** → Using NYU’s calendar export/ICS links for small datasets. Less scalable, but aligned with site features.  
- **Partnership with NYU IT** → Requesting official access to structured event feeds. Provides long-term sustainability. 

---
