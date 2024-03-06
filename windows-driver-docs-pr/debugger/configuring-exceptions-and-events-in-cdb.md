---
title: Configuring Exceptions and Events in CDB
description: You can configure CDB to react to specified exceptions and events in a specific way. For each exception, you can set the break status and the handling status. 
ms.date: 11/28/2017
---

# Configuring Exceptions and Events in CDB


You can configure CDB to react to specified exceptions and events in a specific way. For each exception, you can set the break status and the handling status. For each event, you can set the break status.

You can configure the break status or handling status by doing one of the following:

-   Use the [**SXE**](../debuggercmds/sx--sxd--sxe--sxi--sxn--sxr--sx---set-exceptions-.md), **SXD**, **SXN**, or **SXI** command.

-   Use the **-x**, **-xe**, **-xd**, **-xn**, or **-xi** option on the [**CDB command line**](cdb-command-line-options.md).
-   Use the **sxe** or **sxd** keyword in the Tools.ini file.

For a detailed discussion of exceptions and events, see [Controlling Exceptions and Events](controlling-exceptions-and-events.md).

 

 