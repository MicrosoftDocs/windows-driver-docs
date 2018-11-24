---
title: ScsiInquiry
description: ScsiInquiry
ms.assetid: a4f6f21c-b096-4a2f-a207-e8618682e780
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ScsiInquiry


The **ScsiInquiry** method instructs the miniport driver that manages an iSCSI initiator HBA to issue a SCSI inquiry command to a logical unit on the target and return the results.

This WMI method belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **ScsiInquiry** method, see the member descriptions for the [**ScsiInquiry\_IN**](https://msdn.microsoft.com/library/windows/hardware/ff564593) and [**ScsiInquiry\_OUT**](https://msdn.microsoft.com/library/windows/hardware/ff564602) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class must support **ScsiInquiry**.

 

 





