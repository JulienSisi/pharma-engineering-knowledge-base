# Sezione 3 — Troubleshooting & CAPA in ambiente biologics

## 3.1 Specificità dei guasti in biologics

I modi di guasto in ambiente biologics presentano delle specificità che complicano il troubleshooting rispetto a un ambiente small molecule:

```
Small molecule (Celgene)          Biologics (Lonza Visp)
─────────────────────────────     ──────────────────────────────
Processo chimico deterministico   Processo biologico variabile
Contaminazione chimica misurabile Contaminazione biologica (micoplasmi, bioburden)
Cleaning chimico validato         CIP/SIP critico — integrità biologica
Strumenti classici               Sensori in linea (pH, DO, conduttività, pressione)
Confinamento chimico             Confinamento biologico + HPAPI
```

## 3.2 Strumenti RCA adattati al contesto biologics

### FMEA Bioreattore / Small Equipment

La FMEA in contesto biologics integra modi di guasto specifici:

| Componente | Modo di guasto | Effetto potenziale | RPN guida |
|------------|----------------|-------------------|-----------|
| Giunto peristaltico | Usura → perdita | Contaminazione lotto | Elevato |
| Sonda pH | Deriva calibrazione | CPP fuori limite | Elevato |
| Filtro ventilazione | Intasamento | Pressione differenziale fuori spec | Medio |
| Valvola sterile | Azionamento difettoso | Contaminazione crociata | Elevato |
| Autoclave | Ciclo incompleto | Non-sterilità | Critico |

### Ciclo integrato RCA-CAPA in GMP biologics

```
Segnale qualità / guasto equipaggiamento
              ↓
    Deviazione formale (GMP record)
              ↓
    Investigazione RCA (5M / FMEA / 5 Whys)
              ↓
    Causa radice identificata (sistemica, non superficiale)
              ↓
    Piano CAPA: correzione immediata + azione preventiva
              ↓
    Implementazione + documentazione
              ↓
    Effectiveness check (verifica di efficacia)
              ↓
    Chiusura CAPA → Aggiornamento CMMS + SOP se applicabile
              ↓
    Alimentazione OEE / KPI → ciclo di miglioramento continuo
```

*Figura 3.1 — Ciclo integrato RCA-CAPA-miglioramento continuo in ambiente GMP biologics*

## 3.3 Troubleshooting in produzione commerciale vs. sviluppo

In fase di ramp-up commerciale (contesto Visp 2026), si esercita una pressione aggiuntiva sul troubleshooting: ogni lotto conta, ogni fermata ha un costo contrattuale diretto. L'approccio deve combinare:

- **Reattività**: identificare e contenere rapidamente l'impatto
- **Rigore GMP**: documentare ogni fase nonostante la pressione temporale
- **Profondità di investigazione**: arrivare alla causa radice sistemica per evitare ricorrenze

## 3.4 Competenze RCA-CAPA per il ruolo I&U Engineer Visp

L'analisi della letteratura converge su tre requisiti di maturità:

**Profondità di investigazione** — andare oltre la causa prossimale per identificare i fattori sistemici (progettazione, intervalli PM, condizioni d'uso reali vs. specifiche), basandosi sulla combinazione 5M + FMEA + dati CMMS storici.

**Rigore documentale** — ogni investigazione produce una traccia formale conforme ai requisiti GMP, con raccomandazioni concrete, assegnate, con scadenze e criteri di efficacia misurabili.

**Orientamento al miglioramento continuo** — il CAPA non è una risposta puntuale a un incidente isolato. Alimenta un ciclo di miglioramento delle strategie di manutenzione (intervalli PM, criticità, procedure), dei SOP e degli indicatori OEE/KPI del sito.

L'esperienza di redazione e follow-up di CAPA, deviazioni e SOP acquisita in ambiente GMP API sotto doppia sorveglianza FDA/SwissMedic costituisce un ancoraggio diretto in questo framework.

---

*→ Sezione 4: GMP Utilities biologics — CIP/SIP, WFI, clean steam*

---

### Riferimenti (estratti)

- Seely, R.J. et al. (2021). *Failure analysis biopharmaceutical manufacturing*
- ICH Q9. *Quality Risk Management — FMEA application*
- FDA. *Guidance on deviation and CAPA in biologics manufacturing*