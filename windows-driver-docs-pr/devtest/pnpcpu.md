---
title: PNPCPU
description: PNPCPU
ms.assetid: 397283e6-0691-4e55-9507-483bb311b524
keywords:
- driver testing WDK , PNPCPU
- testing drivers WDK , PNPCPU
- testing drivers WDK , logical processors
- testing drivers WDK , ONECPU
- logical processors WDK
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# PNPCPU


PNPCPU (Pnpcpu.exe) is a command line tool that simulates a hot add of processors to a running instance of Windows Server 2008.

Driver and application developers can use this tool to test that their driver or application does not fail when processors are added at system runtime. In cases where the driver or application has been extended to make use of the Hot Add Processor feature, PNPCPU can be used to confirm that all relevant Plug and Play notifications are handled correctly.

PNPCPU ships in Windows Vista WDK and later, and runs on Windows Server 2008. To use this tool, you must be a member of the Administrators group.

This section includes the following information:

[PNPCPU Overview](pnpcpu-overview.md)

[PNPCPU General Commands](pnpcpu-general-commands.md)

[PNPCPU Typical Session](pnpcpu-typical-session.md)

[PNPCPU General Notes](pnpcpu-general-notes.md)

[PNPCPU Limitations](pnpcpu-limitations.md)

 

 





