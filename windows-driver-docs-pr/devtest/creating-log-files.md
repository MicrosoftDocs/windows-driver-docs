---
title: Creating Log Files
description: Creating Log Files
ms.assetid: dad0f9fc-1a88-4bee-800a-5a4464fff600
keywords:
- log files WDK Driver Verifier
- Driver Verifier WDK , log files
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Creating Log Files


## <span id="ddk_creating_log_files_tools"></span><span id="DDK_CREATING_LOG_FILES_TOOLS"></span>


Driver Verifier can create log files. These files will contain periodic updates on a number of statistics related to Driver Verifier's actions and the actions of the drivers being verified.

Log files are created from the Verifier utility by using the **/log** parameter. The frequency of the log record can be specified as well. See [**Verifier Command Line**](verifier-command-line.md) for details.

Each entry will contain both global counters and individual counters, just as with the **verifier /query** command.

For an explanation of these statistics, see [Monitoring Global Counters](monitoring-global-counters.md) and [Monitoring Individual Counters](monitoring-individual-counters.md).

 

 





