---
title: Myriad of machines that had a user mode crash or hang
description: This measure evaluates myriad (out of 10,000) of machines encountering a user mode crash or hang from a list of the tracked apps in graphics driver binary.
ms.date: 10/10/2025
ms.topic: troubleshooting-known-issue
---

# Myriad of machines that had a user mode crash or hang

## Description

This measure evaluates myriad (out of 10,000) of machines encountering a user mode crash or hang from a list of the tracked apps in graphics driver binary.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7-day sliding window |
| **Measurement criteria** | Aggregation of machines |
| **Minimum population** | 10,000 machines |
| **Passing criteria** | <= 60/10,000 machines experience a user mode crash or hang |
| **Measure ID** | 55580311 |

## Calculation

This measure evaluates myriad (out of 10,000) of machines encountering a user mode crash or hang from a list of the tracked apps in graphics driver binary.

1. Machines that crashed = count(machines that experienced a user mode crash or hang)
1. Total machines = count(machines)
1. Ratio of crashed machines = machines that crashed / total machines
