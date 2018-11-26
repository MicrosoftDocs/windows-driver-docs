---
title: Logging scenarios
description: This topic describes logging scenarios for user-initiated feedback with IHV trace logging in WDI drivers.
ms.assetid: B9E10527-9C25-46B6-ADC2-4CF5AB749E04
ms.date: 06/15/2018
ms.localizationpriority: medium
---

# Logging scenarios

The events saved in IHV log files, for both repro mode and the auto-logger, should be appropriately throttled via flags/level/keywords to ensure that at least the past 30 minutes of the log events are always saved. Practically, you should target the 30 minute time period to cover one scan/WFD discovery, one connect/roam event, one disconnect event, several power transitions, and 10 minutes' worth of send and receive data. Because the IHV repro mode log is much larger than the normal IHV auto-logger, more verbose logging is expected.

The following scenarios might help you when logging:

- Getting connected
- Power transitions
- Radio management
- Roaming
- Hang/recovery
- Transition from Connected to Limited

## Related links

[User-initiated feedback with IHV trace logging](user-initiated-feedback-with-ihv-trace-logging.md)
