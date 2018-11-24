---
title: RunAs
description: RunAs
ms.assetid: 47183A50-513C-4bc5-8DC4-33065323F584
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# RunAs


TAEF provides a mechanism to execute tests Elevated, Restricted, as Local System or within a Low Integrity process.

## <span id="Prerequisites"></span><span id="prerequisites"></span><span id="PREREQUISITES"></span>Prerequisites


-   [Te.Service](te-service.md) must be installed and running on the machine in order to run elevated tests from a non-elevated process, run non-elevated tests from an elevated process, or to run tests as Local System.

## <span id="RunAs_Types"></span><span id="runas_types"></span><span id="RUNAS_TYPES"></span>RunAs Types


TAEF supports the following RunAs types, which are specified via test metadata or the command prompt.

-   [RunAs Elevated](runas-elevated.md)
-   [RunAs LowIL](runas-lowil.md)
-   [RunAs Restricted](runas-restricted.md)
-   [RunAs System](runas-system.md)

 

 





