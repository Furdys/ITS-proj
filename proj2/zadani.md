GUI testy
=========

Cíl
---

Vytvořte automatické testy (Selenium) pro vámi navrženou testovací sadu na 
základě BDD scénářů.

Úkoly
-----

1. Nastudujte integrované prostředí pro tvorbu testů Selenium IDE:

    [ITS10] Přednáška ITS ve 10. týdnu LS 2017/18
    [SeleniumIDE] http://www.seleniumhq.org/projects/ide/
    [SeleniumPythonBindings] http://selenium-python.readthedocs.io/

1.1 Nainstalujte si Selenium IDE pro Chrome nebo Firefox.

    Potřebujete prohlížeč Firefox s nainstalovaným rozšířením Selenium IDE. Na
    stránce http://www.seleniumhq.org/download/ hledejte "Selenium IDE". V
    době psaní zadání byla aktuální verze 3.0.1.

1.2 Vytvořte si zkušební test principem nahrání (record+replay) v Selenium IDE.

    Zajímavé odkazy pro verze Selenium IDE <3.0:

    [SeleniumDocs] http://www.seleniumhq.org/docs/02_selenium_ide.jsp
    [SeleniumYoutube]
    https://www.youtube.com/results?search_query=selenium+ide

    Někdy pro identifikaci objektů/cílů pro příkazy Selenia nestačí
    identifikace poskytnutá skrz Selenium IDE (name, id, link text), ale je
    potřeba identifikaci upřesnit. K tomu může posloužit CSS selektor nebo
    výraz XPath.

    [CSSSelectors] http://www.w3schools.com/cssref/css_selectors.asp
    [ChromeConsoleXPath]
    https://stackoverflow.com/questions/22571267/how-to-verify-an-xpath-expression-in-chrome-developers-tool-or-firefoxs-firebug/22571294
    [XPath] http://www.w3schools.com/xpath/

1.3 Nainstalujte si projekt behave [Behave] pro automatizaci BDD testů. Vyzkoušejte
    si základní příklad [BDDHello].

    [Behave] https://behave.readthedocs.io/en/latest/install.html
    [BDDHello] https://behave.readthedocs.io/en/latest/tutorial.html

1.4 Nainstalujte si rozhraní Selenium pro jazyk Python (modul selenium).

    [PyPi] https://pypi.python.org/pypi/selenium
    [RTDInstall] https://selenium-python.readthedocs.org/installation.html

    V případě, že nemáte počítač s administrátorským přístupem:
    [PipUser] https://pip.pypa.io/en/latest/user_guide.html#user-installs

1.5 Upravte test v jazyce Python pro spuštění na Selenium Server.

    Používejte selenium.webdriver.Remote. Inspirujte se na [RTDSeServer] a
    příkladem [WDMys]. Selenium server/grid pro účely projektu ITS je
    na [ITSSS]. Spouštěč testů (WebDriver, DesiredCapabilities) může být buď
    FIREFOX i CHROME (k dispozici jsou oba).

    Časový limit pro čekání na DOM elementy je doporučen max 15 sekund.

    [ITSSS] http://mys01.fit.vutbr.cz:4444/wd/hub
    [RTDSeServer]
    https://selenium-python.readthedocs.org/getting-started.html#using-selenium-with-remote-webdriver
    [WDMys] https://www.fit.vutbr.cz/study/courses/ITS/private/mys01.py

2. Implementujte automatizované testy vaší sekce testované aplikace.

2.1 Testy budou zahrnovat vámi navržené testy v testovacím plánu odevzdaným
    v prvním projektu. Implementované testy nemusí byt úplně stejné, jako testy
    popsané v návrhu testů v testovacím plánu.

    Zajímavé odkazy:
    [SeleniumPractices]
    https://mestachs.wordpress.com/2012/08/13/selenium-best-practices/
    [PageObject]
    http://blog.activelylazy.co.uk/2011/07/09/page-objects-in-selenium-2-0/
    [PageObjectEx]
    https://weblogs.java.net/blog/johnsmart/archive/2010/08/09/selenium-2web-driver-land-where-page-objects-are-king

2.2 Testy ověřte na (a přizpůsobte ke) spuštění na vzdáleném Selenium Server.

    Daný selenium server [ITSSS] je připraven pro hodnocení projektů.
    Připravte proto testy pro toto běhové prostředí.

3. Sepište report (volitené).

   Report není povinný. Report sepište, pokud:
     * jste našli nějakou chybu (report musí obsahovat popis chyby), nebo
     * pokud se implementované testy liší od navržených testů v 1. projektu.
   V jiném případě report nepište.

3.1 Požadavky na report:

  Formát reportu je PDF, rozsah 1-3 strany. Report obsahuje následující části:

  1. hlavičku,
  2. testy v původním plánu neimplementované,
  3. testy implementované a nepopsané v původním plánu,
  3.1 popis nových testů.
  4. nalezené chyby v podobě stručného hlášení o chybách (bug report).

  Pokud by nějaká část měla být prázdná, do reportu ji nezahrnujte.

4. Odevzdejte své řešení prostřednictvím archivu xLOGIN99.zip. Archiv bude
   obsahovat:

    -/                  kořenový adresář archivu
     +- report.pdf      (nepovinný) report z testování
     +- features/
        +- *.feature    soubory se scénáři
        +- steps/
           +- *.py      soubory s kroky Python-Selenium


   Pro spuštění testů ! na Selenium Serveru [ITSSS] ! musí být úspěšně
   provedeny tyto kroky:

   $ unzip xLOGIN99.zip
   $ behave
