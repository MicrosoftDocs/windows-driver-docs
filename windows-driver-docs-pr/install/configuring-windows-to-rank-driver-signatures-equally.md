---
title: Configuring Windows to Rank Driver Signatures Equally
description: Configuring Windows to Rank Driver Signatures Equally
ms.assetid: 727ad66d-b8f3-4e22-b51f-af9571ae0ec8
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Configuring Windows to Rank Driver Signatures Equally


The [AllSignersEqual Group Policy](allsignersequal-group-policy--windows-vista-and-later-.md) controls [how Windows ranks drivers](how-setup-ranks-drivers.md) that are signed by Microsoft versus drivers that are signed by third-party vendors. When the AllSignersEqual Group Policy is enabled, Windows views all Microsoft signature types and third-party signatures as equal in rank when it selects the driver that is the best match for a device.

**Note**  In Windows Vista and Windows Server 2008, the **AllSignersEqual** Group Policy is disabled by default. Starting with Windows 7, this Group Policy is enabled by default.

 

After you enable the AllSignersEqual Group Policy, this configuration change applies to all subsequent driver installations on the target system until you disable the AllSignersEqual Group Policy.

For more information about how to configure the **AllSignersEqual** Group Policy to rank driver signatures equally, see [AllSignersEqual Group Policy (Windows Vista and Later)](allsignersequal-group-policy--windows-vista-and-later-.md).

 

 





