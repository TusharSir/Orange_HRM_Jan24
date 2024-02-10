pytest -v --html=HTMLReports/myReport_chrome.html --alluredir="AllureReports" -n=2 --browser chrome
pytest -v --html=HTMLReports/myReport_firefox.html --alluredir="AllureReports" -n=2 --browser firefox
pytest -v --html=HTMLReports/myReport_edge.html --alluredir="AllureReports" -n=2 --browser edge
