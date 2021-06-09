---
title: ScsiInquiry
description: ScsiInquiry
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# ScsiInquiry


The **ScsiInquiry** method instructs the miniport driver that manages an iSCSI initiator HBA to issue a SCSI inquiry command to a logical unit on the target and return the results.

This WMI method belongs to the unpublished [MSiSCSI\_Operations WMI class](msiscsi-operations-wmi-class.md). For a description of the parameters of the **ScsiInquiry** method, see the member descriptions for the [**ScsiInquiry\_IN**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_scsiinquiry_in) and [**ScsiInquiry\_OUT**](/windows-hardware/drivers/ddi/iscsiop/ns-iscsiop-_scsiinquiry_out) structures.

Miniport drivers that implement the MSiSCSI\_Operations WMI class must support **ScsiInquiry**.

 

