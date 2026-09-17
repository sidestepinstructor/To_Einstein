Cold Fold — governance runtime
A runnable implementation of the governance architecture described in Cold Fold v7.0 — The Shadow Governor: three engines (System / Phoenix / Einstein) operating under two governors — Cold Fold v7.0, the shadow governor, and Cold Fold v8.0, the silent sovereign.

Cold Fold runtime trace

Five-panel runtime trace of the reference scenario. (a) system coherence against its setpoint; (b) coherence drift against the v7 entry thresholds; (c) identity recursion instability against the v8 entry thresholds, with paradox activity marked; (d, e) the two governor state ladders. Grey bands are shadowseal, dark bands sovereignseal.

Run it
Double-click RUN_COLDFOLD.bat. It runs the engine, then renders the figure, and leaves the outputs in this folder.

From a terminal, equivalently:


python coldfold_engine.py     # writes coldfold_trace.csv
python make_coldfold_fig.py   # re-runs the sim and writes the figure
Requirements. Python 3.9 or newer. The engine itself uses only the standard library — no installs needed. The figure step needs matplotlib (python -m pip install matplotlib); if pypdfium2 is also present the PNG is rendered from vector PDF, otherwise it is written directly at 300 dpi.

What's in the folder
file	what it is
coldfold_engine.py	the engines, the two governors, telemetry, thresholds, scenario
make_coldfold_fig.py	imports the engine and renders the five-panel trace
RUN_COLDFOLD.bat	double-click runner for both of the above
COLDFOLD_SPEC.md	implementation notes: what came from the document, what didn't
coldfold_trace.csv	full 120-tick telemetry of the reference run
coldfold_trace.png / .pdf	the figure
The reference run
The default scenario applies a slow coherence bleed at tick 20, escalates it at tick 40, injects a contradictory constraint at 46, withdraws the disturbance at 62, then diverges identity recursion at 78 and again at 104. The governors respond:

tick	governor	seal	cause	telemetry
50	v7	shadowseal	—	drift 0.1297, paradox 0
52	v8	sovereignseal	shadow governance exhausted	recursion 0.0592
104	v8	sovereignseal	recursion instability	recursion 0.2467
112	v8	sovereignseal	recursion instability	recursion 0.3326
The run is deterministic — there is no random input anywhere in the engine, so coldfold_trace.csv is reproducible byte-for-byte on any machine.

Important caveat on the numbers
The source document specifies state names and escalation laws. It does not specify transition conditions, telemetry definitions, or any thresholds.

Every number in the Thresholds dataclass is therefore an operational choice made to render the prose executable — not a value derived from the plates:

threshold	value	what it gates
coherence_setpoint	0.90	the System engine's target
drift_warn	0.05	v7 DAMPEN entry
drift_freeze	0.14	v7 FREEZE entry
paradox_bind	1	v7 COUNTER entry
recursion_warn	0.10	v8 ANALYZE entry
recursion_sovereign	0.28	v8 SOVEREIGN entry
drift_ewma_alpha	0.35	drift smoothing
recursion_window	8	recursion instability window
They are marked OPERATIONAL in the source and catalogued in COLDFOLD_SPEC.md, which separates section by section what was taken from the document from what was invented to fill a gap. Read that file before treating any tick number above as a property of Cold Fold rather than a property of these threshold choices. Changing a threshold changes the escalation timeline; the ordering of the escalations is the part that follows from the document's laws.

Cold Fold v7 Document Review
Needs your approval
