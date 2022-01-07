---
title: Idle Power Management Assumptions
description: Idle Power Management Assumptions
ms.date: 04/20/2017
---

# Idle Power Management Assumptions

A disk spin up operation completes within 240 seconds (4 minutes) from the time the SCSI Start Unit command is issued to the LUN.

The following SCSI commands (SRB_FUNCTION_EXECUTE_SCSI operations) are expected to complete without requiring the disk to be spun up. In other words, no prior SCSI Start Unit command is required.

- INQUIRY

- REPORT LUNS

Miniport drivers are expected to complete all SRBs except SRB_FUNCTION_IO_CONTROL, SRB_FUNCTION_FLUSH, and SRB_FUNCTION_SHUTDOWN when the LUN is in a low power state.
