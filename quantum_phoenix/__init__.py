from .Phoenix import Phoenix
name: "Phoenix Ignition Cycle"
description: "Initiate a new Phoenix ignition cycle with defined operator intent and module targets."
title: "[IGNITION] <Cycle Name>"
labels: ["ignition", "phoenix", "engine"]
assignees: ["@quantumonix"]

body:
  - type: markdown
    attributes:
      value: |
        ## 🔥 Phoenix Ignition TOE
        Declare your ignition intent and define the cycle parameters below.
        Each field corresponds to a variable in the TOE prompt schema.

  - type: input
    id: operator_intent
    attributes:
      label: "Operator Intent"
      description: "Describe the purpose or goal of this ignition cycle."
      placeholder: "e.g., Initialize Einstein Engine core sequence"

  - type: dropdown
    id: module_targets
    attributes:
      label: "Module Targets"
      description: "Select which engine modules to activate."
      options:
        - Einstein Engine
        - Phoenix Engine
        - Dynamo Engine
        - Hybrid Cycle

  - type: dropdown
    id: scoring_mode
    attributes:
      label: "Scoring Mode"
      description: "Choose the evaluation logic for this cycle."
      options:
        - Deterministic
        - Stochastic
        - Hybrid

  - type: textarea
    id: cue_card_hooks
    attributes:
      label: "Cue‑Card Hooks"
      description: "Optional: define cue‑card seeds or logic triggers."
      placeholder: "e.g., Flame resonance, Operator truth vector"

  - type: textarea
    id: artifact_expectations
    attributes:
      label: "Artifact Output Expectations"
      description: "Specify what the engine should emit after ignition."
      placeholder: "e.g., Codex relic, cycle report, scoring matrix"

  - type: markdown
    attributes:
      value: |
        ---
        **Note:** This issue template enforces ignition‑cycle discipline and routes all submissions through the Phoenix TOE schema.
