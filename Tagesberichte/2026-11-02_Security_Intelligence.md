# DubraSec Security Intelligence Tagesbericht – 02.11.2026

Berichtszeitraum: 01.11.2026, 00:10 Uhr bis 02.11.2026, 00:10 Uhr MEZ (Europe/Berlin). Recherche-/Quellenstand: bis zum Redaktionsschluss öffentlich zugängliche Veröffentlichungen; einzelne Ereignisse haben vor dem Berichtsfenster begonnen und werden ausschließlich wegen neuer Meldungen im Berichtsfenster nachgeführt. Vorausschau: 02.11. bis einschließlich 09.11.2026. Qualitatives OSINT-Lagebild, keine amtliche Gefahrenwarnung. Nicht gefundene Meldungen sind kein Beleg für das Ausbleiben von Vorfällen.

## Management Summary – Lage auf einen Blick

GESAMTRISIKO: ERHÖHT für die externe physische und Cyber-Sicherheitslage. Für nachweislich exponierte Kölner Innenstadtstandorte ist nach den Vorfällen vom 31.10. eine anlassbezogene Nachkontrolle angezeigt; für nicht exponierte Liegenschaften ist keine pauschale Hochstufung begründet. Für AXA, YNCORIS, DLR, Infraserv Hürth und Chemiepark Knapsack wurde in den ausgewerteten öffentlichen Quellen kein neuer gezielter Angriff im Berichtsfenster verifiziert. Risikostufen sind Analysteneinschätzungen und keine behördlichen Einstufungen.

KERNAUSSAGE 1 – KÖLN: Die am 01.11. um 13:25 Uhr veröffentlichte vorläufige Polizeibilanz nennt 23 verletzte Polizeikräfte, Beschädigungen an fünf Streifenwagen, eingeschlagene Geschäftsverglasung sowie mehrere sichergestellte gefährliche Gegenstände. Die Polizei unterscheidet ausdrücklich zwischen vielen friedlichen Versammlungsteilnehmenden und Personen, die nach Versammlungsende Einsatzkräfte angriffen; außerdem beschreibt sie eigenständige, nach derzeitigem Stand nicht mit der Versammlung verbundene nächtliche Randalierergruppen. Eine konkrete Betroffenheit von AXA ist nicht belegt. Originalquelle Polizei Köln, 01.11.: https://www.presseportal.de/blaulicht/pm/12415/6381831

KERNAUSSAGE 2 – BUNDESWEIT: Die Bundespolizei bilanzierte am 01.11. Versammlungslagen in 34 Städten; die Schwerpunkte lagen nach ihrer Darstellung in Hannover, Hamburg, Köln, Frankfurt und Berlin. Ihre Angaben zu Plünderungsversuchen in Köln und Frankfurt sind als Versuche zu kennzeichnen, nicht als bestätigte vollendete Plünderungen. Originalquelle Bundespolizeipräsidium, 01.11.: https://www.presseportal.de/blaulicht/pm/73990/6381813

KERNAUSSAGE 3 – CYBER/LIEFERKETTE: Am 01.11. wurde über eine mögliche Betroffenheit von Malaysia-Airlines-Kundendaten infolge eines Sicherheitsvorfalls beim Reservierungstechnikdienstleister Amadeus berichtet. Nach Aussage der Fluggesellschaft seien eigene IT-Systeme nicht kompromittiert; der Umfang möglicher Datenabflüsse ist noch offen. Quelle Reuters, 01.11.: https://www.reuters.com/legal/litigation/malaysia-airlines-says-customers-may-be-affected-by-amadeus-breach-2026-11-01/ ; ergänzende Wiedergabe der Unternehmensstellungnahme: https://www.thestar.com.my/news/nation/2026/11/01/039our-system-not-compromised-despite-vendor039s-cybersecurity-breach039-says-malaysian-airlines

KERNAUSSAGE 4 – KRITIS INTERNATIONAL: Reuters berichtete am 01.11. über erneute Angriffe auf ukrainische Strominfrastruktur mit umfangreichen Versorgungsunterbrechungen sowie Drohnenschäden an einer nicht näher benannten Industrieanlage in Russland. Angaben zu Angriffsumfang und Zielzuordnung stammen teilweise von Kriegsparteien und sind entsprechend zu behandeln. Quelle Reuters, 01.11.: https://www.reuters.com/world/europe/russian-strikes-cut-power-thousands-ukraine-drones-damage-russian-facility-2026-11-01/

7-TAGE-AUSBLICK: 02.11. Konzert Placebo in Köln-Deutz; 04.11. Champions-League-Spiel Dortmund/Real Betis mit polizeilich angekündigten Verkehrsbeeinträchtigungen; 05.11. von der CGT angekündigter französischer Streik-/Protesttag; 05.–07.11. weitere Arena-Veranstaltungen in Köln, 08.11. Konzert. Ein konkreter neuer Gewaltausbruch an diesen Terminen ist nicht belegt. Veranstalter Köln: https://www.lanxess-arena.de/events-tickets/eventliste-drucken ; Polizei Dortmund: https://www.presseportal.de/blaulicht/pm/4971/6380893 ; Gewerkschaft CGT: https://www.cgt.fr/actualites/france/mobilisation/5-novembre-retrouvez-les-mobilisations-pres-de-chez-vous

PRIORISIERTE MASSNAHMEN: (1) Kölner Innenstadtliegenschaften und exponierte Eingänge vor Wiederaufnahme des Regelbetriebs auf Glas-/Fassadenschäden, provisorische Öffnungen, Verschluss, EMA und Zugangswege prüfen; (2) nur bei konkreter lokaler Exposition zusätzliche Revierfahrt bzw. Wachsamkeit des Sicherheitsdienstes erwägen; (3) Cyber-Drittparteien und betroffene Reservierungs-/Cloud-Dienste auf tatsächliche Abhängigkeit prüfen; (4) selbstgehostete GitLab-/Ruby-Installationen auf CVE-2026-97229 und wirksame Laufzeit-Patches prüfen; (5) Dienstreisen/Veranstaltungen in Dortmund, Frankreich und Köln mit Verkehrs- und Lageinformationen abgleichen. Technische Quelle GitLab/Alpine: https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html

## A. Physische Sicherheit, KRITIS und öffentliche Ordnung – neue Meldungen

### 01 | KÖLN – Aktualisierte Bilanz zu Protestnachwirkungen und Halloween

Ereignisdatum: 31.10. bis in die Nacht zum 01.11.2026. Veröffentlichungsdatum: 01.11.2026, 13:25 Uhr. Ort: Köln, insbesondere Innenstadt und Umfeld Konrad-Adenauer-Ufer. Nach Angaben der Polizei wurden nach Ende der Versammlung bei nahezu 1.000 Personen Identitäten festgestellt. Aus der kontrollierten Gruppe wurden Einsatzkräfte mit Flaschen, Steinen und Knallkörpern beworfen; bei Kontrollen fanden Einsatzkräfte unter anderem Stichwaffen, Nothämmer, selbstgebaute Pyrotechnik und Molotowcocktails. Die Polizei meldet insgesamt 23 verletzte Beamte und fünf beschädigte Streifenwagen. Getrennt davon beschreibt sie nächtliche Gruppen, die unter anderem eine Geschäftsfensterfront zerstörten, Müllcontainer anzündeten und Barrikaden errichteten. Die Polizei sieht nach derzeitigem Kenntnisstand keinen Bezug dieser eigenständigen Gruppen zu den Versammlungsteilnehmenden. Ob aus Geschäften Gegenstände entwendet wurden, war zum Meldungszeitpunkt Gegenstand der Ermittlungen.

Faktenstatus: OFFIZIELLE VORLÄUFIGE POLIZEIBILANZ; konkrete strafrechtliche Schuldzuordnungen und Schadenhöhe offen. Relevanz: HOCH für exponierte innerstädtische Gebäude, Empfang, Schaufenster, Zufahrten und Sachwerte; eine AXA-Betroffenheit wurde nicht belegt. Risikoeinschätzung: ERHÖHT für lokale Nachwirkungen und unerkannte Gebäudeschäden, nicht automatisch für alle Standorte. Empfehlung: gezielte Schadensnachschau und Sicherung; Anzeige und Beweissicherung bei Feststellungen; bei Schäden Absprache mit First Line und Werkschutz; keine pauschale Zuschreibung der Taten an die gesamte Versammlung.

Originalquelle Polizei Köln, 01.11.2026: https://www.presseportal.de/blaulicht/pm/12415/6381831
Vorherige Zwischenbilanz 31.10.2026 (zum Vergleich): https://www.presseportal.de/blaulicht/pm/12415/6381520

### 02 | DEUTSCHLAND – Bundespolizei bilanziert 34 Versammlungsorte

Ereignisdatum: 31.10.2026; neue bundesweite Bilanz veröffentlicht am 01.11.2026, 12:44 Uhr. Die Bundespolizei berichtet über Versammlungslagen in 34 deutschen Städten, Unterstützung der Länderpolizeien durch mehr als 600 Bundesbereitschaftspolizisten sowie mehr als 2.000 Einsatzkräfte im eigenen Zuständigkeitsbereich. Nach ihrer Bilanz erlitten 52 Bundespolizisten bei Unterstützungseinsätzen und drei im eigenen Bereich leichte Verletzungen. Sie berichtet unter anderem über versuchte Plünderungen in Köln/Frankfurt sowie Barrikaden und Steinwürfe in Hamburg. Diese Angaben dürfen nicht als Beleg vollendeter Plünderungen in Köln interpretiert werden.

Faktenstatus: BUNDESPOLIZEILICHE EINSATZBILANZ; Details können sich mit weiteren Länderpolizei-Ermittlungen ändern. Relevanz: MITTEL bis HOCH für Filialen, öffentlich zugängliche Gebäude, Sicherheitskommunikation und Ereignisnachbereitung. Risiko: lokal differenziert; kein Nachweis einer bundesweit koordinierten Attacke gegen Versicherer. Empfehlung: bei möglichen Folgedemonstrationen aktuelle Polizei-/Versammlungsinformationen vor Ort prüfen; keine automatisierte Gleichsetzung von Protest und Gewalt.

Originalquelle Bundespolizeipräsidium, 01.11.2026: https://www.presseportal.de/blaulicht/pm/73990/6381813

### 03 | STUTTGART – Polizei meldet Straftaten nach überwiegend friedlicher Versammlung

Ereignisdatum: 31.10.2026; neue Bilanz 01.11.2026, 14:26 Uhr. Nach Angaben des Polizeipräsidiums Stuttgart nahmen etwa 6.000 Menschen teil, überwiegend friedlich. Zugleich wurden rund 50 Straftaten und sieben verletzte Polizeikräfte registriert. Die Polizei nennt Farbschmierereien, Angriffe auf Einsatzkräfte, brennende Mülltonnen sowie den Versuch, die Scheibe einer Bankfiliale am Marienplatz einzuwerfen.

Faktenstatus: VORLÄUFIGE POLIZEIBILANZ; Täterermittlungen offen. Relevanz: MITTEL für innerstädtische AXA-Standorte und die Versicherungsbranche als Schutz-/Schadenpräventionsszenario, ohne nachgewiesenen AXA-Schaden. Risiko: MITTEL für exponierte Fassaden in der Nachschau, keine pauschale fortdauernde Gefahrenlage. Empfehlung: auf konkrete lokale Sachschäden und Folgeankündigungen achten.

Originalquelle Polizeipräsidium Stuttgart, 01.11.2026: https://www.presseportal.de/blaulicht/pm/110977/6381847

### 04 | HAMBURG – Nachträgliche Polizeibilanz zu Versammlung und Halloween

Ereignisdatum: 31.10.2026; Veröffentlichung 01.11.2026, 00:30 Uhr und damit im Berichtsfenster. Die Polizei Hamburg berichtet von etwa 6.700 Teilnehmenden an einem Aufzug und späteren Störungen mit Pyrotechnik, Steinwürfen und einem entzündeten Kleinfeuer aus entwendeten Absperrelementen. Die Vorgänge sind örtlich und zeitlich von anderen Halloween-Ereignissen zu unterscheiden.

Faktenstatus: POLIZEILICHE EINSATZABSCHLUSSMELDUNG mit möglichen späteren Ermittlungsänderungen. Relevanz: MITTEL für innerstädtische Liegenschaften und Veranstaltungs-/Verkehrssicherheit. Risiko: nach dem Ereignis standortbezogen, kein pauschaler Hinweis auf Folgetaten. Empfehlung: nur bei konkret betroffenen Gebäuden Nachkontrolle und Lageabgleich.

Originalquelle Polizei Hamburg, 01.11.2026: https://www.presseportal.de/blaulicht/pm/6337/6381547

### 05 | UKRAINE / RUSSLAND – Erneute Angriffe auf Energie- und Industrieanlagen

Ereignisdatum: Nacht 31.10./01.11.2026; Veröffentlichung Reuters 01.11.2026. Reuters berichtet unter Berufung auf ukrainische Behörden von Angriffen auf Strominfrastruktur in vier Regionen mit Ausfällen für zahlreiche Haushalte. Ein russischer Gouverneur meldete nach einem ukrainischen Drohnenangriff erhebliche Schäden an einer nicht näher benannten Industrieanlage in der Region Nischni Nowgorod. Eine konkrete Betroffenheit der dort gelegenen Raffinerie darf aus dieser Meldung nicht als bestätigt abgeleitet werden.

Faktenstatus: INTERNATIONALE NACHRICHTENAGENTUR, wesentliche Lagezahlen/Angriffszuordnungen beruhen auf Angaben der Konfliktparteien; unabhängig nur begrenzt überprüfbar. Relevanz: MITTEL für KRITIS-Resilienz, Versorgungsketten, Reise- und Energiepreisrisiken; keine direkte Betroffenheit der beobachteten deutschen Organisationen belegt. Risiko: ERHÖHT für betroffene Kriegsgebiete, MITTEL als indirektes Abhängigkeitsrisiko. Empfehlung: Abhängigkeiten von Energie, Logistik und kritischen Dienstleistern im BCM prüfen; keine unbelegten konkreten Versorgungswarnungen für Deutschland aussprechen.

Quelle Reuters, 01.11.2026: https://www.reuters.com/world/europe/russian-strikes-cut-power-thousands-ukraine-drones-damage-russian-facility-2026-11-01/

## B. Cyberangriffe, Lieferketten, Versicherungen und Sicherheitslücken

### 06 | AMADEUS / MALAYSIA AIRLINES – Potenzieller Kundendatenabfluss über Drittanbieter

Ereignisdatum: exakter Angriffszeitpunkt nicht veröffentlicht; betroffene Datenverarbeitung laut Airline möglicherweise zwischen August 2023 und September 2026. Veröffentlichung/öffentliche Berichterstattung: 01.11.2026; die Airline-Stellungnahme wurde laut Medien am 31.10. abgegeben. Malaysia Airlines erklärte, dass nach einem Sicherheitsvorfall beim Reservierungstechnologie-Anbieter Amadeus möglicherweise bestimmte Kundendaten betroffen seien. Eigene IT-Systeme seien nicht kompromittiert; bislang gebe es keinen Beleg für Zugriff auf Finanzdaten. Umfang, Ursache und betroffene Personenzahl sind nicht abschließend bekannt.

Faktenstatus: DURCH AIRLINE-STELLUNGNAHME BESTÄTIGTER DRITTPARTEIEN-VORFALL; konkrete Datenexfiltration bei einzelnen Kunden noch nicht vollständig nachgewiesen. Relevanz: HOCH als übertragbares Drittparteien-/Datenschutzszenario für Versicherer und Travel Security; keine direkte AXA- oder DLR-Betroffenheit belegt. Risiko: ERHÖHT für möglicherweise betroffene Reisendendaten; ansonsten MITTEL als Lieferantenrisiko. Empfehlung: Reisebuchungs-/TMC-Dienstleisterinventar auf Amadeus-Abhängigkeiten prüfen; auf offizielle Benachrichtigungen warten; Beschäftigte bei tatsächlicher Betroffenheit zu Phishing sensibilisieren.

Quelle Reuters, 01.11.2026: https://www.reuters.com/legal/litigation/malaysia-airlines-says-customers-may-be-affected-by-amadeus-breach-2026-11-01/
Wiedergabe Airline-Stellungnahme, The Star, 01.11.2026: https://www.thestar.com.my/news/nation/2026/11/01/039our-system-not-compromised-despite-vendor039s-cybersecurity-breach039-says-malaysian-airlines

### 07 | GITLAB / ALPINE LINUX – Neue Fachberichterstattung und akuter Prüfbedarf

Ereignisdatum: Ausnutzungsversuche 20./21.10.2026; Primärmeldung Alpine 28.10., Betreiber-Update 30.10.; neue fachjournalistische Einordnung am 01.11.2026. Alpine Linux berichtet, dass Angreifer CVE-2026-97229 auf der eigenen GitLab-Instanz auszunutzen versuchten. Alpine fand keinen Beleg für erfolgreiche Codeausführung, kann diese mangels vollständiger Logs jedoch nicht ausschließen und baute die Instanz vorsorglich neu auf. Bei selbstgebauten GitLab-Images kann eine GitLab-Versionsaktualisierung allein unzureichend sein, wenn die verwundbare Ruby-Laufzeit unverändert bleibt. Die Schwachstelle steht seit 29.10. im CISA-Katalog bekanntermaßen ausgenutzter Schwachstellen; die dort genannte US-Bundesbehörden-Frist 01.11. ist keine deutsche allgemeine Rechtsfrist.

Faktenstatus: PRIMÄRQUELLE ALPINE BESTÄTIGT VERSUCHE UND VORSORGEMASSNAHMEN, KEIN BESTÄTIGTER ERFOLGREICHER EINBRUCH; CISA KEV als Priorisierungshinweis. Relevanz: HOCH für selbstgehostete GitLab-/CI-CD-Umgebungen, Softwarelieferketten und kritische Entwicklungsprozesse; keine AXA-Nutzung dieser verwundbaren Konfiguration belegt. Risiko: HOCH bei exponierter verwundbarer Installation, sonst anlagenabhängig. Empfehlung: tatsächliche GitLab- und Ruby-Version prüfen, Herstellerpatch einspielen, Internetexposition und Logs kontrollieren, bei Verdacht Secrets rotieren und forensische Bewertung durchführen.

Primärquelle Alpine Linux, 28./30.10.2026: https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html
Hersteller-Release GitLab: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/
Fachbericht vom 01.11.2026: https://www.bleepingcomputer.com/news/security/alpine-linux-rebuilds-gitlab-after-attempted-rce-attack/
CISA KEV-Katalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog

### 08 | DEUTSCHLAND – Ransomware-Behauptungen nicht als bestätigte Vorfälle werten

Veröffentlichungsdatum der geprüften Übersicht: 01.11.2026. Die integrisec-Chronik enthält im November neue Einträge, erklärt jedoch selbst, dass diese auf Täterveröffentlichungen und nicht auf Bestätigungen betroffener Unternehmen beruhen. Deshalb werden daraus keine neuen verifizierten Unternehmensangriffe oder Schadenssummen abgeleitet.

Faktenstatus: NICHT UNABHÄNGIG BESTÄTIGTE TÄTERBEHAUPTUNGEN. Relevanz: MITTEL als Beobachtungssignal, nicht als belegter Schadenfall. Risiko: NICHT BEWERTBAR für einzeln genannte mutmaßliche Opfer ohne Bestätigung. Empfehlung: offizielle Unternehmens-, CERT- oder Behördenbestätigung abwarten; keine Namen aus Leak-Seiten als feststehende Opfer kommunizieren.

Quelle mit ausdrücklichem Methodikhinweis, Stand 01.11.2026: https://integrisec.de/cyberangriffe/

## C. Beobachtete Organisationen und Personen – Prüfergebnis

### 09 | AXA, YNCORIS, DLR, Infraserv Hürth und Chemiepark Knapsack

Prüfzeitraum: 01.11.2026, 00:10 Uhr bis 02.11.2026, 00:10 Uhr MEZ. Bei der selektiven Recherche öffentlich zugänglicher Unternehmens-, Polizei-, Behörden- und Medienquellen wurde keine neue, belastbar verifizierte direkte physische oder Cyberattacke auf AXA Deutschland/AXA Gruppe, YNCORIS, DLR, Infraserv Hürth oder den Chemiepark Knapsack im Berichtsfenster gefunden. Dies ist ausdrücklich ein NEGATIVER RECHERCHEBEFUND und keine Bestätigung der Vorfallsfreiheit. Der Bezug der Kölner Ereignisse zu AXA-Standorten bleibt unbestätigt.

Faktenstatus: RECHERCHEBEFUND MIT EINGESCHRÄNKTER ABDECKUNG. Relevanz: HOCH für laufende standortbezogene Beobachtung. Risiko: keine zusätzliche organisationsspezifische Hochstufung ohne belastbare Informationen. Empfehlung: First-Line-Lage- und Schadensmeldungen mit OSINT abgleichen; neue offizielle Vorfallsmeldungen priorisiert nachführen.

Offizielle Prüfeinstiege: https://www.axa.de/presse ; https://www.dlr.de/ ; https://www.presseportal.de/blaulicht/nr/12415
Hinweis: Eine verifizierte konkrete YNCORIS-Primärmeldung zum Berichtsfenster wurde nicht gefunden.

### 10 | AXA Konzern AG – verifizierter Vorstand, keine neuen belegten Vorwürfe

Die offizielle AXA-Seite führt Dr. Thilo Schumacher, Irina Buchmann, Dr. Achim Dahlbokum, Dr. Johannes Dick, Dr. Karsten Dietrich, Kayum Guerrero, Stephanie Peterson, Daniela-Carina Pohl und Dr. Marc Daniel Zimmermann als Mitglieder des Konzernvorstands. Für diese namentlich verifizierten Personen wurde im Berichtsfenster keine neue belastbar verifizierte sicherheitsrelevante Negativmeldung gefunden. Keine personenbezogenen Mutmaßungen werden aufgenommen.

Faktenstatus: VORSTANDSNAMEN OFFIZIELL VERIFIZIERT; NEGATIVER RECHERCHEBEFUND ohne Vollständigkeitsgarantie. Relevanz: MITTEL für Executive Security und Reputationsmonitoring. Risiko: keine neue personenspezifische Gefährdung belegbar. Empfehlung: offizielle Organmeldungen und relevante glaubwürdige Berichterstattung weiter beobachten.

Originalquelle AXA Konzernvorstand: https://www.axa.de/wir-ueber-uns/konzernvorstand-und-aufsichtsrat

## D. Vorausschauende Sicherheitslage – 02.11. bis 09.11.2026

### V01 | 02.11. – Köln-Deutz: Placebo in der LANXESS arena

Geplantes Datum/Ort: Montag 02.11.2026, 20:00 Uhr, LANXESS arena Köln-Deutz; Einlass 18:00 Uhr. Bestätigungsstatus: VERANSTALTERTERMIN BESTÄTIGT. Mögliche Auswirkungen: lokale Anreise-/Abreisefrequenz und Parkraumauslastung; keine konkrete Gewaltwarnung. Betroffene Organisationen: nur bei tatsächlich benachbarten Liegenschaften oder Dienstwegen; AXA-Betroffenheit nicht nachgewiesen. Risiko: NIEDRIG bis MITTEL für Verkehrs-/Zugangssituation, Eintritt konkreter Störungen ungewiss. Empfehlung: Anfahrt und Zufahrten bei betroffenen Standorten prüfen.

Originalquelle LANXESS arena: https://www.lanxess-arena.de/eventdetail/1357

### V02 | 04.11. – Dortmund: Champions League Borussia Dortmund gegen Real Betis

Geplantes Datum/Ort: Mittwoch 04.11.2026, Anstoß 21:00 Uhr, Signal Iduna Park Dortmund. Bestätigungsstatus: POLIZEILICH BESTÄTIGTE VERANSTALTUNG; die Polizei erwartet erfahrungsgemäß Verkehrsstörungen um Stadion, Innenstadt und Zufahrten. Eine Ausschreitung ist damit nicht prognostiziert. Betroffene Organisationen: Dienstreisende, mögliche Standorte/Servicefahrten im Dortmunder Umfeld. Risiko: MITTEL für Verkehrs- und Logistikbeeinträchtigungen; Gewaltlage NICHT BELEGT. Empfehlung: alternative Wege, Pufferzeiten und ÖPNV prüfen.

Originalquelle Polizei Dortmund, 30.10.2026: https://www.presseportal.de/blaulicht/pm/4971/6380893

### V03 | 05.11. – Frankreich: angekündigter Streik- und Demonstrationstag

Geplantes Datum/Ort: Donnerstag 05.11.2026, landesweite französische Mobilisierungen, lokale Zeiten je Veranstalterkarte. Bestätigungsstatus: GEWERKSCHAFTSAUFRUF BESTÄTIGT; tatsächliche Beteiligung, einzelne Sperrungen und Folgen noch offen. Betroffene Organisationen: AXA-Gruppe/Frankreichbezug, internationale Dienstreisen und grenzüberschreitende Lieferketten; konkrete Beeinträchtigung einzelner AXA-Standorte NICHT BELEGT. Risiko: MITTEL für Mobilität und mögliche lokale Betriebseinschränkungen, Eintritt standortbezogen ungewiss. Empfehlung: 04./05.11. französische Betreiber- und Polizeihinweise prüfen, Reisepläne flexibel halten; friedliche Demonstrationen nicht mit Gewaltereignissen gleichsetzen.

Originalquelle CGT, 30.10.2026: https://www.cgt.fr/actualites/france/mobilisation/5-novembre-retrouvez-les-mobilisations-pres-de-chez-vous
Ergänzende CGT-Aufrufbegründung, 21.10.2026: https://www.cgt.fr/comm-de-presse/la-cgt-appelle-generaliser-la-greve-le-5-novembre

### V04 | 05.–08.11. – Köln-Deutz: weitere bestätigte Arena-Veranstaltungen

Geplantes Datum/Ort: 05., 06. und 07.11.2026 jeweils 20:00 Uhr Felix Lobrecht; 08.11.2026 19:30 Uhr The World of Hans Zimmer, LANXESS arena Köln-Deutz. Bestätigungsstatus: VERANSTALTERKALENDER BESTÄTIGT. Die Arena nennt außerdem temporäre Parkplatz-P5-Sperrungen am 04.–08.11.; kurzfristige Änderungen sind möglich. Betroffene Organisationen: nur tatsächlich betroffene Anfahrts-/Zufahrtswege und Standorte. Risiko: NIEDRIG bis MITTEL für Parken und Verkehr, kein belegtes sicherheitskritisches Gewaltszenario. Empfehlung: Besucher- und Dienstwege bei Bedarf zeitlich entzerren.

Originalquelle Veranstalterkalender: https://www.lanxess-arena.de/events-tickets/eventliste-drucken
Originalquelle P5-Sperrungen: https://www.lanxess-arena.de/anfahrt-parken/anfahrt-mit-pkw/parkplatz-p5

### V05 | 02.–09.11. – GitLab-Sicherheitslücke CVE-2026-97229 als fortlaufende Cyberpriorität

Zeitraum: sofortiger Prüfbedarf, kein einzelnes angekündigtes Angriffsdatum. Bestätigungsstatus: SCHWACHSTELLE UND ANGRIFFSVERSUCHE DURCH HERSTELLER/BETREIBER BELEGT; ein spezifisch bevorstehender Angriff auf AXA oder deutsche KRITIS ist NICHT BELEGT. Mögliche Auswirkungen: Codeausführung bei verwundbaren selbstgehosteten GitLab-Instanzen, Abfluss von CI-Secrets, Störung von Build-Pipelines. Risiko: HOCH bei betroffenen exponierten Instanzen, sonst abhängig von Inventar. Empfehlung: versions- und laufzeitgenaue Prüfung; technische Patchvalidierung und ggf. Secret-Rotation.

Originalquellen GitLab/Alpine: https://docs.gitlab.com/releases/patches/patch-release-gitlab-19-4-2-released/ ; https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html

### V06 | Weitere Protest- und Sabotageankündigungen im Beobachtungsraum

Für 02.–09.11.2026 konnte in den selektiv geprüften Quellen keine weitere hinreichend konkret bestätigte standortbezogene Protest-, Blockade- oder Sabotageankündigung für AXA, YNCORIS, DLR, Infraserv Hürth oder Chemiepark Knapsack nachgewiesen werden. Das ist kein Beleg für das Ausbleiben kurzfristiger Anmeldungen oder spontaner Ereignisse. Risiko: OFFEN, keine spekulative Erhöhung. Empfehlung: täglich lokale Versammlungsbehörden, Polizei, Betreiberhinweise und Sicherheitsdienste prüfen; offene Ereignisse vom 31.10. als Nachverfolgung weiterführen.

Quellen zum Nachverfolgen: https://www.presseportal.de/blaulicht/nr/12415 ; https://www.presseportal.de/blaulicht/nr/4971 ; https://www.cgt.fr/actualites/france/mobilisation/5-novembre-retrouvez-les-mobilisations-pres-de-chez-vous

## E. Priorisierte Empfehlungen, Faktenstatus und Nachverfolgung

PRIORITÄT 1 / PHYSISCH: Kölner Innenstadtlagen mit realer Exposition zum Geschehen vom 31.10. auf Einbruchspuren, Glasschäden, Sachbeschädigung und Verschlussmängel prüfen; Schäden dokumentieren und First Line/Polizei melden. Nur bei konkreter Risikokonstellation zusätzliche Revierfahrt prüfen. Basis: https://www.presseportal.de/blaulicht/pm/12415/6381831

PRIORITÄT 2 / CYBER: GitLab CE/EE und selbstgebaute Images auf CVE-2026-97229, tatsächlich gepatchte Ruby-Laufzeit, exponierte CI-Runner und Secret-Verwaltung prüfen; vorhandene technische Prozesse statt pauschaler Alarmierung nutzen. Basis: https://alpinelinux.org/posts/GitLab-security-incident-CVE-2026-97229.html

PRIORITÄT 3 / DRITTPARTEIEN: Bei tatsächlichen Amadeus-/Reisebuchungsabhängigkeiten mögliche Lieferantenmeldungen, Datenschutzfolgen und Phishing-Risiken prüfen; keine Betroffenheit ohne belastbare Mitteilung unterstellen. Basis: https://www.reuters.com/legal/litigation/malaysia-airlines-says-customers-may-be-affected-by-amadeus-breach-2026-11-01/

PRIORITÄT 4 / VORAUSSCHAU: Für Dortmund 04.11., Frankreich 05.11. und Köln-Deutz 02.–08.11. Verkehrs-/Zugangspläne an bestätigten Veranstaltungsinformationen ausrichten. Basis: https://www.presseportal.de/blaulicht/pm/4971/6380893 ; https://www.cgt.fr/actualites/france/mobilisation/5-novembre-retrouvez-les-mobilisations-pres-de-chez-vous ; https://www.lanxess-arena.de/events-tickets/eventliste-drucken

NACHVERFOLGUNG: (a) Kölner Polizei-Ermittlungen und Schadensbilanz: OFFEN; (b) Amadeus-Datenumfang: OFFEN; (c) Alpine/GitLab: Schwachstelle bestätigt, konkrete organisationsbezogene Exposition OFFEN; (d) Frankreich 05.11.: AUFRUF BESTÄTIGT, tatsächliche Durchführung/Verkehrsfolgen offen; (e) neue Gen-Z-Folgeversammlungen: keine verifizierte konkrete Ankündigung in dieser Recherche. Quellen jeweils in den Abschnitten unmittelbar zugeordnet.

## Methodik und Abgrenzung

Öffentliche Quellen werden nach Veröffentlichungsdatum und Ereignisdatum getrennt. Primärquellen (Polizei, Betreiber, Veranstalter, Hersteller) haben Vorrang; Nachrichtenagenturen werden für internationale Entwicklungen ergänzend genutzt. Zahlen aus Konfliktgebieten und unbestätigte Täterangaben sind gekennzeichnet. Der Bericht erhebt keinen Anspruch auf vollständige Erfassung aller Meldungen oder sämtlicher Standorte. Nicht belegte Personen- oder Unternehmensvorwürfe werden nicht übernommen.