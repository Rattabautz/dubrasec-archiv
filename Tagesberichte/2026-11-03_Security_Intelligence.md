# DubraSec Security Intelligence Tagesbericht – 03.11.2026

Berichtszeitraum: 02.11.2026, 00:10 Uhr bis 03.11.2026, 00:10 Uhr MEZ (Europe/Berlin). Redaktionsstand: unmittelbar vor dem geplanten Abschluss um 00:10 Uhr. Ausblick: 03.11. bis 10.11.2026, 00:10 Uhr. Öffentliche OSINT-Auswahl; keine amtliche Gefahrenwarnung. Frühere Ereignisse erscheinen nur bei neuer Veröffentlichung oder einer ausdrücklich bezeichneten Nachverfolgung. Nicht aufgefundene Berichte beweisen nicht das Ausbleiben eines Vorfalls.

## Management Summary – Lage auf einen Blick

GESAMTRISIKO: ERHÖHT als qualitative Bewertung der externen Cyber- und KRITIS-Lage; für einzelne exponierte IT-/OT-Systeme bei nachgewiesener Verwundbarkeit HOCH. Keine öffentlich belegte akute, gezielte Bedrohung gegen AXA, YNCORIS, DLR oder den Chemiepark Knapsack im geprüften Zeitfenster. Lokale Veranstaltungsrisiken sind überwiegend NORMAL bis MITTEL, abhängig von Standort und Anreise. Diese Bewertungen sind analytische Einschätzungen, keine amtlichen Warnstufen.

KERNAUSSAGE 1 – EUROPÄISCHE KÜHLKETTEN: Reuters berichtete am 02.11. über Störungen von vernetzten Kühl- und Gefrieranlagen in mehr als 100 europäischen Einzelhandelsstandorten. Mehrere Unternehmen sprechen von Cybervorfällen. Die technische Ursache, die Täterschaft und ein möglicher Zusammenhang der einzelnen Fälle sind nicht abschließend festgestellt. Für Versicherer sind Betriebsunterbrechungs-, Warenverderb- und Gebäudetechnik-Risiken relevant. Originalquellen mit Unternehmensangaben über Reuters, 02.11.: https://www.reuters.com/business/european-retailers-hit-by-supermarket-fridge-hack-2026-11-02/ und https://www.reuters.com/business/retail-consumer/temperature-soars-swedish-grocery-store-freezers-one-store-blames-hackers-2026-11-02/

KERNAUSSAGE 2 – VPN-ANGRIFFSKETTE: Am 02.11. veröffentlichten Rapid7 und HKCERT neue fachliche bzw. behördliche Einordnungen zu bereits aktiv ausgenutzten Ivanti-Connect-Secure-Schwachstellen CVE-2026-104935, CVE-2026-111357 und CVE-2026-118527. Die Aufnahme der beiden letztgenannten Schwachstellen in CISA KEV erfolgte bereits am 30.10.; dies ist eine neue Lagebewertung, keine neue Entdeckung am 02.11. Relevanz HOCH für tatsächlich betroffene exponierte VPN-Geräte. Quellen: https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527/ ; https://www.hkcert.org/security-bulletin/ivanti-connect-secure-multiple-vulnerabilities_20261102 ; https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog

KERNAUSSAGE 3 – UKRAINISCHE ENERGIE-KRITIS: Amnesty International warnte am 02.11. vor den humanitären Folgen der intensivierten Angriffe auf Strom- und Wärmeinfrastruktur in der Ukraine. Die Organisation stützt ihre Bewertung auf dokumentierte frühere Angriffe und UN-Angaben; nicht alle aktuellen Einzelereignisse sind unabhängig geprüft. Primärquelle, 02.11.: https://www.amnesty.org/en/latest/news/2026/11/ukraine-russias-increased-attacks-on-energy-and-heating-infrastructure-creating-a-deadly-situation-for-civilians/

KERNAUSSAGE 4 – WARNINFRASTRUKTUR: Eine am 02.11. erschienene Berichterstattung beschreibt manipulierte Warnmeldungen in ukrainischen Notfall-Apps nach dem Vorfall vom 01.11.; die Behörden hatten vorübergehend einen Kanal deaktiviert. Täterzuschreibungen sind nicht verifiziert. Relevanz: Integrität redundanter Alarmierung. Quellen: https://www.theguardian.com/world/2026/nov/02/hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app ; Hintergrund Reuters 01.11.: https://www.reuters.com/world/europe/ukrainian-air-force-says-public-air-raid-alert-app-has-been-hacked-2026-11-01/

KERNAUSSAGE 5 – VORAUSSCHAU: Die vom DLR mitorganisierte Weltraumrobotik-Konferenz findet 03.–06.11. im Kölner Confex statt. Für 04.11. bestätigt die Polizei Dortmund ein Champions-League-Spiel mit Reise-/Verkehrsbezug; für 05.11. ruft die französische CGT zu landesweiten Streiks und Demonstrationen auf. Eine Gewaltentwicklung ist durch diese Ankündigungen nicht belegt. Originalquellen: https://event.dlr.de/en/event/joint-i-sairas-isparo-conference-2026/ ; https://www.presseportal.de/blaulicht/pm/4971/6380893 ; https://www.cgt.fr/actualites/france/mobilisation/5-novembre-retrouvez-les-mobilisations-pres-de-chez-vous

PRIORISIERTE EMPFEHLUNGEN: (1) Betreiber exponierter Ivanti-Connect-Secure-VPNs auf tatsächliche Nutzung, Fixstand und mögliche Kompromittierungsindikatoren prüfen; (2) vernetzte Kühl-/Gebäudetechnik und deren Fernzugänge in Risiko- und Dienstleisterinventaren berücksichtigen; (3) redundante Warnkanäle und die Authentizität von Alarmmeldungen sicherstellen; (4) DLR-Konferenz und Kölner Arena-Veranstaltungen im standortbezogenen Verkehrs-/Besuchermanagement berücksichtigen; (5) Reisen und kritische Lieferketten mit Frankreichbezug am 05.11. anhand aktueller Betreiberinformationen bewerten. Keine generelle Gefahrenhochsetzung für friedliche Versammlungen.

## A. Physische Sicherheit und kritische Infrastruktur – neue Veröffentlichungen

### 01 | UKRAINE – Amnesty dokumentiert Risiken für Energie- und Wärmeversorgung

Ereignisdatum: Mehrere Angriffe in Oktober 2026 und fortdauernde Angriffsserie; neue Veröffentlichung: 02.11.2026. Amnesty International beschreibt erneute Angriffe auf ukrainische Strom- und Heizungsinfrastruktur vor dem Winter und verweist unter anderem auf UN-Monitoring. Die Zahlen und Bewertungen zu früheren Angriffen sind als Angaben der Organisation bzw. ihrer zitierten Quellen zu verstehen; dies ist keine Meldung über einen einzigen neuen Angriff vom 02.11.

Faktenstatus: BESTÄTIGTE VERÖFFENTLICHUNG einer internationalen Menschenrechtsorganisation; einzelne militärische Angriffsdetails sind nicht unabhängig durch diesen Bericht verifiziert. Relevanz: HOCH für KRITIS-Resilienz in betroffenen Kriegsgebieten; MITTEL als Vergleichs- und Abhängigkeitsszenario für deutsche Standorte. Risiko: HOCH für betroffene Regionen; keine konkrete deutsche Ausfallprognose. Empfehlung: Abhängigkeiten von Strom, Heizung, Telekommunikation, Wasser und Ersatzversorgung im BCM zusammen betrachten.

Originalquelle Amnesty International, veröffentlicht 02.11.2026: https://www.amnesty.org/en/latest/news/2026/11/ukraine-russias-increased-attacks-on-energy-and-heating-infrastructure-creating-a-deadly-situation-for-civilians/

### 02 | RUSSLAND – Neue Reservekapazitätsregel für Rechenzentren nach früheren Angriffen

Ereignisdatum: Unterschrift unter Regierungsdekret am oder vor dem 02.11.2026; Reuters-Veröffentlichung: 02.11.2026. Reuters berichtet über eine Vorgabe, wonach private russische Rechenzentren 10 Prozent Kapazität für staatlich abrufbare IT-Reserven vorhalten sollen. Der Bericht stellt den Zusammenhang zu früheren Drohnenangriffen auf russische Rechenzentren im Oktober her. Die Maßnahme selbst ist kein neuer Angriff und wird als Resilienz-/Regulierungsentwicklung eingeordnet.

Faktenstatus: AGENTURBERICHT über staatliche Regelung; Details der praktischen Umsetzung offen. Relevanz: MITTEL als internationales Beispiel für staatlich angeordnete IT-Reserven; keine unmittelbar belegte Auswirkung auf deutsche Versicherungs- oder Chemieparkstandorte. Risiko: MITTEL als geopolitisches Abhängigkeits-/Souveränitätsthema. Empfehlung: Internationale Hosting-Abhängigkeiten und regulatorische Zugriffsmöglichkeiten im Lieferantenmanagement differenziert betrachten.

Quelle Reuters, veröffentlicht 02.11.2026: https://www.reuters.com/technology/putin-orders-private-data-centres-set-aside-10-capacity-support-it-2026-11-02/

## B. Cyberangriffe, OT und Lieferketten – neue Veröffentlichungen

### 03 | EUROPA – Cybervorfälle an Kühlanlagen im Lebensmitteleinzelhandel

Ereignisdatum: Nacht 01./02.11. bis 02.11.2026; Reuters-Veröffentlichungen: 02.11.2026. Mehrere europäische Einzelhändler meldeten gestörte Kühl- und Gefrieranlagen. Reuters nennt unter anderem Delhaize, Carrefour, Colruyt, Coop, ICA und Musgrave; teilweise mussten gekühlte Waren aus dem Verkauf genommen werden. Die Zahl der Standorte und Auswirkungen sind vorläufig. Dass alle Störungen technisch zusammenhängen oder einem einzigen Angreifer zuzurechnen sind, ist nicht nachgewiesen. Betroffenheit einzelner Danfoss-basierter Systeme ist kein Beleg für eine herstellerseitige Sicherheitslücke.

Faktenstatus: MEHRFACHE UNTERNEHMENSAUSSAGEN über Reuters, Ermittlungen laufen; Täterschaft und gemeinsamer Angriffsweg offen. Relevanz: HOCH für industrielle/gebäudetechnische Fernwartung, Lebensmittelversorgung, Sach- und Betriebsunterbrechungsversicherung. Risiko: ERHÖHT für vernetzte Kühlanlagen mit ungeprüften Fernzugängen; keine generelle Warnung für alle OT-Anlagen. Empfehlung: Remote-Zugänge, Alarmgrenzen, Temperaturmonitoring, Segmentierung und Notbetrieb anlagenbezogen prüfen; Lieferantenmeldungen abgleichen.

Quellen Reuters, veröffentlicht 02.11.2026: https://www.reuters.com/business/european-retailers-hit-by-supermarket-fridge-hack-2026-11-02/ ; https://www.reuters.com/business/retail-consumer/temperature-soars-swedish-grocery-store-freezers-one-store-blames-hackers-2026-11-02/

### 04 | IVANTI CONNECT SECURE – Fach-/CERT-Update zu ausgenutzten VPN-Schwachstellen

Ereignisdatum: Ausnutzung nach Angaben von Sicherheitsforschern bereits Anfang Oktober 2026; Ivanti-Update 29.10., CISA-KEV-Eintrag 30.10.; neue Veröffentlichungen von Rapid7 und HKCERT am 02.11.2026. Die Schwachstellen CVE-2026-104935, CVE-2026-111357 und CVE-2026-118527 können in einer Angriffskette zusammenwirken. Für bestimmte Versionen liegen Updates vor. Rapid7 verweist auf beobachtete Kompromittierungen und empfiehlt priorisierte Behebung. Die CISA-Fristen gelten spezifisch für US-Bundesbehörden und sind nicht als pauschale deutsche Rechtsfrist darzustellen.

Faktenstatus: DURCH HERSTELLER, CERT UND SICHERHEITSFORSCHER BELEGTE AKTIVE AUSNUTZUNG; keine Betroffenheit von AXA oder anderen beobachteten Organisationen belegt. Relevanz: HOCH für internetexponierte VPN-Gateways, Remote-Zugänge und IT-Drittparteien. Risiko: HOCH nur bei verwundbaren betroffenen Installationen; sonst konfigurationsabhängig. Empfehlung: Produktinventar, Firmwarestände, Hersteller-Fixversionen, Indikatoren für Kompromittierung und ggf. Incident-Response-Prozess prüfen.

Primärnahe Quellen, 02.11.2026: https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527/ ; https://www.hkcert.org/security-bulletin/ivanti-connect-secure-multiple-vulnerabilities_20261102 ; Herstellerhinweis: https://hub.ivanti.com/s/article/Security-Advisory-Ivanti-Connect-Secure-CVE-2026-104935?language=en_US ; CISA-Mitteilung 30.10.: https://www.cisa.gov/news-events/alerts/2026/10/30/cisa-adds-two-known-exploited-vulnerabilities-catalog

### 05 | UKRAINE – Manipulierte Notfallwarnungen, am 02.11. weiter berichtet

Ereignisdatum: 01.11.2026 (außerhalb des 24-Stunden-Fensters); neue Berichterstattung: 02.11.2026. Nach Angaben ukrainischer Stellen wurden in einer ergänzenden Warn-App falsche Warnungen vor nuklearen, chemischen und militärischen Gefahren verbreitet. Ein betroffener App-Kanal wurde zeitweise abgeschaltet, andere Warnwege blieben nutzbar. Eine namentlich behauptete Täterschaft ist nicht unabhängig verifiziert; die russische Seite meldete einen gesonderten ähnlichen Vorfall.

Faktenstatus: BEHÖRDLICH BESTÄTIGTE STÖRUNG, Täter unbekannt; Nachverfolgung eines älteren Ereignisses, nicht neuer Angriff am 02.11. Relevanz: HOCH für Vertrauen in Alarmierungs- und Warnketten, MITTEL für die beobachteten Organisationen. Risiko: ERHÖHT für alleinige Abhängigkeit von einem digitalen Warnkanal. Empfehlung: Authentizität von Warnungen über unabhängige Behördenkanäle prüfen und mehrere Alarmierungswege vorhalten.

Quelle Guardian, veröffentlicht 02.11.2026: https://www.theguardian.com/world/2026/nov/02/hackers-fake-nuclear-chemical-threat-alert-kyiv-ukraine-emergency-app ; Reuters-Hintergrund vom 01.11.2026: https://www.reuters.com/world/europe/ukrainian-air-force-says-public-air-raid-alert-app-has-been-hacked-2026-11-01/

## C. Versicherungsbranche, AXA und beobachtete Organisationen

### 06 | VERSICHERUNGEN – Indirekte Schaden- und Cyberexposition durch Kühlkettenvorfälle

Ereignis-/Veröffentlichungsdatum: 02.11.2026. Die öffentlich berichteten Kühlanlagenstörungen können je nach Deckung und Kausalität Fragen zu Warenverderb, technischen Anlagen, Betriebsunterbrechung und Cyberdeckung aufwerfen. Konkrete Versicherungsansprüche, Schadenhöhen einzelner Versicherer oder eine AXA-Betroffenheit sind NICHT öffentlich belegt. Dies ist eine fachliche Risikofolgerung, kein gemeldeter AXA-Schaden.

Faktenstatus: ANALYTISCHE ABLEITUNG aus bestätigten Betreiberberichten; keine bestätigten AXA-Schadenzahlen. Relevanz: MITTEL bis HOCH für Versicherungswirtschaft. Risiko: MITTEL, abhängig von tatsächlicher Deckung und Schadenumfang. Empfehlung: Keine konkreten Schadenbeträge oder Versichererzuordnungen ohne offizielle Meldung kommunizieren.

Grundlage Reuters, 02.11.2026: https://www.reuters.com/business/european-retailers-hit-by-supermarket-fridge-hack-2026-11-02/

### 07 | AXA / VORSTAND – Kein neuer öffentlich verifizierter negativer Vorfall im Fenster

Berichtszeitraum: 02.11. 00:10 bis 03.11. 00:10 MEZ. Bei der gezielten Recherche wurde keine neue, hinreichend belegte negative Sicherheitsmeldung zu AXA Deutschland, AXA Gruppe oder namentlich verifizierten aktuellen AXA-Führungskräften identifiziert. Die offizielle AXA-Seite führt unter anderem Thomas Buberl als CEO im Management Committee mit Stand 01.09.2026. Die Feststellung ist ein Recherche-Negativbefund und kein Beleg für Ereignisfreiheit. Keine unbelegten personenbezogenen Vorwürfe.

Faktenstatus: RECHERCHE-NEGA­TIVBEFUND; Führungszuordnung anhand AXA-Primärquelle. Relevanz: Laufendes Monitoring. Risiko: Kein Anlass zur unternehmensspezifischen Hochstufung aus den geprüften Quellen. Empfehlung: Neue Unternehmens-, Behörden- und belastbare Medienmeldungen im Folgebericht prüfen.

AXA-Primärquelle zur Verifikation des Managements: https://www.axa.com/about-us/executive-management

### 08 | YNCORIS, CHEMIEPARK KNAPSACK, DLR, INFRASERV HÜRTH – Monitoring ohne belegten Angriff

Berichtszeitraum: 02.11.2026. In den ausgewerteten öffentlichen Quellen wurde keine neue belegte Attacke gegen YNCORIS, den Chemiepark Knapsack oder das DLR im Berichtsfenster festgestellt. YNCORIS bezeichnet sich als Betreiber des Chemieparks Knapsack und Nachfolger der früheren InfraServ Knapsack; „Infraserv Hürth“ wurde nicht als eigenständiger aktueller Betreiber verifiziert. DLR ist über die angekündigte Konferenz 03.–06.11. konkret im Ausblick vertreten. Ein fehlender Treffer ist kein Entwarnungsnachweis.

Faktenstatus: RECHERCHE-NEGATIVBEFUND und verifizierte Betreiber-/Veranstalterangaben. Relevanz: HOCH für standortbezogenes Monitoring, aber kein nachgewiesener aktueller Vorfall. Risiko: Keine neue unternehmensspezifische Hochstufung begründet. Empfehlung: Betreiber- und Behördenmeldungen fortlaufend verfolgen; Veranstaltungen nicht als Bedrohung deklarieren.

YNCORIS-Unternehmensprofil: https://www.yncoris.com/yncoris-auf-einen-blick/ ; DLR-Veranstaltungskalender: https://event.dlr.de/en/event/joint-i-sairas-isparo-conference-2026/

## D. Vorausschauende Sicherheitslage – 03.11. bis 10.11.2026

### V01 | 03.–06.11.2026 – DLR / i-SAIRAS & iSpaRo in Köln-Deutz

Geplantes Datum: 03.–06.11.2026. Ort: Confex Cologne, Barmer Straße 20, 50679 Köln. Die vom DLR mitorganisierte Fachkonferenz für Weltraumrobotik und KI ist offiziell angekündigt. Bestätigungsstatus: VERANSTALTERBESTÄTIGT; Durchführung und etwaige spätere Änderungen vorbehalten. Mögliche Betroffenheit: DLR, internationale Teilnehmende, Veranstaltungsort und Reise-/Verkehrsinfrastruktur Köln-Deutz; AXA/YNCORIS nur indirekt bei konkreter lokaler Exposition. Eintrittsunsicherheit: Veranstaltung hoch plausibel, Störung oder Gewalt NICHT belegt. Risiko: NORMAL bis MITTEL wegen Besucher- und Verkehrsaufkommen. Empfehlung: reguläre Besucher-, Anreise- und Zutrittsprozesse; keine pauschale Gefahrenannahme.

DLR-Primärquelle mit Ort/Termin: https://event.dlr.de/en/event/joint-i-sairas-isparo-conference-2026/

### V02 | 04.11.2026 – Fußballgroßveranstaltung Dortmund

Geplantes Datum: 04.11.2026, 21:00 Uhr. Ort: Signal Iduna Park, Dortmund. Die Polizei Dortmund hat das Champions-League-Spiel Borussia Dortmund gegen Real Betis und Faninformationen angekündigt. Bestätigungsstatus: POLIZEILICH ANGEKÜNDIGT; Verkehr und Fanströme können örtlich beeinflusst werden. Mögliche Betroffenheit: Dienstreisen, Mitarbeitende, Veranstaltungs- und ÖPNV-Wege in Dortmund. Eintrittsunsicherheit: Spiel angekündigt; konkrete Störungen oder Gewalt nicht belegt. Risiko: NORMAL bis MITTEL für Anreiseplanung. Empfehlung: aktuelle Polizei- und Verkehrsinfos berücksichtigen, ohne Fangruppen pauschal zu kriminalisieren.

Polizei Dortmund, 30.10.2026: https://www.presseportal.de/blaulicht/pm/4971/6380893

### V03 | 05.11.2026 – Frankreichweite Streik- und Demonstrationsaufrufe

Geplantes Datum: 05.11.2026. Ort: mehrere französische Städte, einzelne Versammlungsorte in der CGT-Karte. Die CGT ruft zu landesweiten Arbeitsniederlegungen und Demonstrationen auf. Bestätigungsstatus: GEWERKSCHAFTLICHER AUFRUF; tatsächliche Teilnahme, konkrete Verkehrsausfälle und örtliche Durchführung noch unsicher. Mögliche Betroffenheit: AXA Frankreich, internationale Dienstreisen, grenzüberschreitende Logistik, kritische Zulieferer. Eintrittsunsicherheit: Aufruf bestätigt, tatsächliche Störungen nicht pauschal prognostizierbar. Risiko: MITTEL für Reise- und Betriebsplanung bei Frankreichbezug; Gewaltprognose NICHT belegt. Empfehlung: lokale Betreiber- und Behördenmeldungen prüfen, Reisealternativen vorbereiten und friedlichen Protest nicht mit Gewalt gleichsetzen.

CGT-Primärquelle, veröffentlicht 30.10.2026: https://www.cgt.fr/actualites/france/mobilisation/5-novembre-retrouvez-les-mobilisations-pres-de-chez-vous

### V04 | 05.–08.11.2026 – Arena-Veranstaltungen Köln-Deutz

Geplante Daten: 05., 06. und 07.11.2026 jeweils Felix Lobrecht, Beginn 20:00 Uhr; 08.11.2026 The World of Hans Zimmer, Beginn 19:30 Uhr. Ort: LANXESS arena, Köln-Deutz. Bestätigungsstatus: VERANSTALTERKALENDER; Änderungen möglich. Mögliche Betroffenheit: Zufahrten und ÖPNV im Umfeld Köln-Deutz, Besuchermanagement, Anreise von DLR-Konferenzteilnehmenden; keine direkte AXA- oder Chemiepark-Betroffenheit belegt. Eintrittsunsicherheit: Veranstaltungen angekündigt; Sicherheitsstörung nicht belegt. Risiko: NORMAL bis MITTEL als Verkehrs-/Besucherlast. Empfehlung: Reisezeiten und alternative Wege prüfen.

Primärquelle LANXESS arena: https://www.lanxess-arena.de/prisma

### V05 | 03.–10.11.2026 – Fortdauerndes Cyberrisiko durch ausgenutzte Ivanti-VPN-Lücken

Zeitraum: laufend während des Ausblicks, kein spezifischer angekündigter Angriffstermin. Ort: weltweit, ausschließlich tatsächlich betroffene Ivanti-Connect-Secure-Installationen. Bestätigungsstatus: AKTIVE AUSNUTZUNG BEREITS DOKUMENTIERT, aber kein konkreter Angriff auf die betrachteten Organisationen oder ein fest angekündigtes neues Angriffsdatum. Mögliche Betroffenheit: Versicherer, Betreiber kritischer Infrastruktur, IT-Dienstleister nur bei entsprechender Nutzung. Eintrittsunsicherheit: anlagenspezifisch; eine allgemeine Angriffswahrscheinlichkeit ist nicht quantifiziert. Risiko: HOCH für verwundbare internetexponierte Systeme. Empfehlung: Patchstand und Kompromittierungsindikatoren zeitnah prüfen, Herstellerwarnungen nachführen.

Rapid7 vom 02.11.2026: https://www.rapid7.com/blog/post/etr-additional-ivanti-connect-secure-zero-days-exploited-in-the-wild-cve-2026-111357-cve-2026-118527/ ; HKCERT vom 02.11.: https://www.hkcert.org/security-bulletin/ivanti-connect-secure-multiple-vulnerabilities_20261102

## E. Nachverfolgung, Methodik und Grenzen

Köln 31.10.: Die bereits am 01.11. veröffentlichte vorläufige Polizeibilanz mit 23 verletzten Einsatzkräften bleibt relevant, aber am 02.11. wurde bei der aktuellen Suche keine neue verifizierte polizeiliche Bilanz identifiziert. Deshalb keine Wiederholung als neue 24-Stunden-Meldung. Originalquelle der älteren Bilanz: https://www.presseportal.de/blaulicht/pm/12415/6381831

Ausblick 05.11. Frankreich: Aufruf weiterhin auf der CGT-Seite sichtbar; konkrete regionale Streikfolgen müssen kurz vor Termin neu verifiziert werden. Originalquelle: https://www.cgt.fr/actualites/france/mobilisation/5-novembre-retrouvez-les-mobilisations-pres-de-chez-vous

Methodik: Nur datierte öffentlich zugängliche Primärquellen, Betreiber-/CERT-Informationen und belastbare Agenturberichte; ausdrücklich genannte Recherchenegativbefunde sind nicht gleichbedeutend mit Nullrisiko. Risikoabschätzungen beruhen auf Exposition, Plausibilität und Folgen und ersetzen weder behördliche Warnungen noch interne Lageinformationen. Bei personenbezogenen Behauptungen keine Zuschreibung ohne unabhängige Bestätigung. Alle Original-URLs stehen unmittelbar bei der jeweiligen wesentlichen Aussage und sind in DOCX/PDF als anklickbare Links vorgesehen.
