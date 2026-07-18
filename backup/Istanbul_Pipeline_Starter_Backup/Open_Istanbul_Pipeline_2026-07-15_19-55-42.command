#!/bin/bash

set -u

PROJECT="$HOME/Documents/GitHub/istanbul-housing-market-analytics-pipeline"
GITHUB_URL="https://github.com/rukiye-erdogan/istanbul-housing-market-analytics-pipeline"
HEPSIEMLAK_URL="https://www.hepsiemlak.com/istanbul-satilik/residence-site-ici"

clear

echo "=============================================="
echo "Istanbul Housing Pipeline Control Center"
echo "=============================================="
echo

if [[ ! -d "$PROJECT" ]]; then
    echo "FEHLER: Projektordner wurde nicht gefunden:"
    echo "$PROJECT"
    echo
    read -r -p "ENTER zum Schließen ..."
    exit 1
fi

cd "$PROJECT" || exit 1

echo "Projektordner: OK"

open "$PROJECT"
echo "Finder: geöffnet"

if [[ -d "/Applications/Visual Studio Code.app" ]]; then
    open -a "Visual Studio Code" "$PROJECT"
    echo "Visual Studio Code: geöffnet"
else
    echo "Visual Studio Code: nicht gefunden"
fi

if [[ -d "/Applications/Telegram 2.app" ]]; then
    open "/Applications/Telegram 2.app"
    echo "Telegram 2: geöffnet"
elif [[ -d "/Applications/Telegram.app" ]]; then
    open "/Applications/Telegram.app"
    echo "Telegram: geöffnet"
else
    echo "Telegram: nicht gefunden"
fi

open -a "Calendar"
echo "Kalender: geöffnet"

open -a "Safari" "$GITHUB_URL"
sleep 1
open -a "Safari" "$HEPSIEMLAK_URL"
echo "Safari: GitHub und Hepsiemlak geöffnet"

echo
echo "----------------------------------------------"
echo "Cronjob:"
crontab -l 2>/dev/null || echo "Kein Cronjob gefunden."

echo
echo "----------------------------------------------"
echo "Letzter Pipeline-Status:"

LATEST_LOG="$(ls -1t "$PROJECT"/logs/pipeline_*.log 2>/dev/null | head -1)"

if [[ -n "${LATEST_LOG:-}" ]]; then
    echo "Log: $LATEST_LOG"
    grep -E \
        "New Listings Found|Pipeline finished successfully|Historical CSV updated" \
        "$LATEST_LOG" 2>/dev/null | tail -5
else
    echo "Noch keine Logdatei gefunden."
fi

echo
echo "=============================================="
echo "Arbeitsumgebung ist vollständig geöffnet."
echo "=============================================="
echo
echo "ENTER = Pipeline jetzt manuell starten"
echo "S     = Überspringen und Terminal offen lassen"
echo "Q     = Starter-Terminal schließen"
echo

read -r -p "Auswahl: " choice

case "$choice" in
    q|Q)
        echo "Starter wird geschlossen."
        exit 0
        ;;

    s|S)
        echo
        echo "Pipeline wurde nicht gestartet."
        echo "Terminal bleibt im Projektordner geöffnet."
        echo
read -r -p "ENTER zum Schließen des Starter-Terminals ..."
        ;;

    "")
        if pgrep -f "[r]un_full_pipeline.sh" >/dev/null 2>&1; then
            echo
            echo "ACHTUNG: Die Pipeline läuft offenbar bereits."
            echo "Ein zweiter paralleler Lauf wird nicht gestartet."
            echo
            echo "Terminal bleibt im Projektordner geöffnet."
            echo
read -r -p "ENTER zum Schließen des Starter-Terminals ..."
        fi

        echo
        echo "Pipeline wird gestartet ..."
        echo "Bei der Browser-Prüfung im Terminal ENTER drücken."
        echo

        ./run_full_pipeline.sh

        status=$?

        echo
        if [[ $status -eq 0 ]]; then
            echo "Pipeline wurde erfolgreich beendet."
        else
            echo "Pipeline wurde mit Fehlercode $status beendet."
            echo "Bitte die angezeigte Fehlermeldung und den neuesten Log prüfen."
        fi

        echo
        echo "Terminal bleibt im Projektordner geöffnet."
        echo
read -r -p "ENTER zum Schließen des Starter-Terminals ..."
        ;;

    *)
        echo
        echo "Ungültige Auswahl. Pipeline wurde nicht gestartet."
        echo "Terminal bleibt im Projektordner geöffnet."
        echo
read -r -p "ENTER zum Schließen des Starter-Terminals ..."
        ;;
esac
