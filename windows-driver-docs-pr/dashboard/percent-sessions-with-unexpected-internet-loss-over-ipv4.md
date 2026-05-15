---
title: Percentage of Sessions With Unexpected Internet Loss Over IPv4
description: The measure aggregates telemetry from a seven-day sliding window into a percentage of instances where there are unexpected disconnects
ms.date: 10/20/2005
ms.topic: concept-article
---

# Percentage of sessions with unexpected Internet loss over IPv4

Unexpected Internet loss can disrupt user productivity, degrade application performance, and signal underlying issues in network stability. This measure tracks how often devices lose IPv4 Internet connectivity after a successful connection has been established. By analyzing telemetry across sessions, Microsoft can identify patterns of instability, validate driver and stack behavior, and guide improvements to ensure a more reliable Ethernet experience.

## Description

Once a device successfully establishes a IPv4 and connects to Internet, the user should expect a stable connection with little to no Internet loss.

## Measure attributes

| Attribute | Value |
|--|--|
| **Audience** | Standard |
| **Time period** | 7 days |
| **Machine vs. Instance** | Instance |
| **Minimum instances** | 100 instances |
| **Passing criteria** | <= 3% of instances end up with unexpected disconnects |
| **Measure ID** | 55883614 |

## Calculation

This measure calculates the percentage of instances, aggregated per device, that have at least one unexpected Internet loss. Internet loss occurs after Internet connectivity is established,
when the Network Connectivity Status Indicator (NCSI) CapabilityChange event is fired during a Dynamic Host Configuration Protocol (DHCP) connectivity session and the previous capability was Internet.
