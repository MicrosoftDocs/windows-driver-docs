---
title: Percent of machines passing TPM critical checks for attestation but might have PCR mismatches
description: This measure is an average aggregation of telemetry from a 28-day sliding window.
ms.date: 03/13/2025
---
 
# Percent of machines passing TPM critical checks for attestation but might have PCR mismatches

## Description

Pre-attestation health check (PAHC) is designed to perform security health diagnostics at every cold boot and hibernate resume scenario, not waiting until the Microsoft attestation service is triggered. This measure leverages PAHC to detect potential issues in new updates that could prevent successful attestation. Potential issues include missing or invalid certificates, boot logs, or mismatching platform configuration registers values. PAHC logs the results for user visibility.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | PAHC measures capture data from any machine with a TPM at every cold boot and hibernate resume running GE OS builds. |
| **Time period** | 28 day sliding window |
| **Machine vs. Instance** | Instance |
| **Minimum Population** | 25 instances |
| **Passing criteria** | >=99% |
| **Measure ID** | 51378333 |

## Calculation

This measure is an average aggregation of telemetry from a 28-day sliding window
