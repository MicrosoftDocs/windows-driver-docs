---
title: IPM Assumptions
description: IPM Assumptions
ms.assetid: 3c8d8121-9987-43d3-b573-4ca1d26fef7d
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# IPM Assumptions


A disk spin up operation completes within 240 seconds (4 minutes) from the time the SCSI Start Unit command is issued to the LUN.

The following SCSI commands (SRB\_FUNCTION\_EXECUTE\_SCSI operations) are expected to complete without requiring the disk to be spun up. In other words, no prior SCSI Start Unit command is required.

INQUIRY

REPORT LUNS

Miniport drivers are expected to complete all SRBs except SRB\_FUNCTION\_IO\_CONTROL, SRB\_FUNCTION\_FLUSH, and SRB\_FUNCTION\_SHUTDOWN when the LUN is in a low power state.

 

 




