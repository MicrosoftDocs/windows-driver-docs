---
title: Text Mode Phase of the Network Upgrade Process
description: Text Mode Phase of the Network Upgrade Process
ms.assetid: 4878e0ae-194a-459c-bebf-75259b1eed2d
keywords: ["network component upgrades WDK , phases", "upgrading network components WDK , phases", "text mode phase WDK networking"]
---

# Text Mode Phase of the Network Upgrade Process


## <a href="" id="ddk-text-mode-phase-of-the-network-upgrade-process-ng"></a>


**Note**  Vendor-supplied network upgrades are not supported in Microsoft Windows XP (SP1 and later), Microsoft Windows Server 2003, and later operating systems.

 

Setup strips all comments from the AnswerFile and writes the AnswerFile to the System32 directory under the name $Winnt$.inf. Then the system boots into GUI mode setup. No network-specific processing occurs during the text mode phase.

 

 





