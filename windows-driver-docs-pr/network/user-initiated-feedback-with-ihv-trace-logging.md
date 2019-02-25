---
title: User-initiated feedback with IHV trace logging
description: This topics in this section outline the steps required for collecting verbose IHV trace logs during user-initiated feedback (UIF) reports submitted via the Feedback tool.
ms.assetid: BDD02AA2-A771-4AC1-B9D2-E9E8FA073B7A
ms.date: 06/15/2018
ms.localizationpriority: medium
---

# User-initiated feedback with IHV trace logging

This topics in this section outline the steps required for collecting verbose IHV trace logs during user-initiated feedback (UIF) reports submitted via the Feedback tool. There are two separate scenarios in which the Feedback tool will collect logs. The first scenario is a snapshot of the system at the time when the user initiates the feedback. During this time, Windows collects the WMI auto-loggers and some other snapshot data. The second scenario involves the user reproducing the issue. During this feedback, Windows starts loggers with more verbose logging and larger file sizes to capture as much data as possible for the repro. This section describes the expectations for IHVs for each of these feedback scenarios.

In this section:

- [Logging scenarios](logging-scenarios.md)
- [User-initiated feedback - normal mode](user-initiated-feedback-normal-mode.md)
- [User-initiated feedback - repro mode](user-initiated-feedback-repro-mode.md)
