---
title: Port monitor client DLL functions
description: Provides information about port monitor client DLL functions.
keywords:
- port monitors WDK print, functions
- client DLL port monitor functions WDK
ms.date: 09/14/2022
---

# Port monitor client DLL functions

The following table lists the functions that a port monitor UI DLL must define.

| Function name | Description |
|--|--|
| **DllEntryPoint** | DLL entry point, typically called **DllMain**, which is described in the Microsoft Windows SDK documentation. |
| [**AddPortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-addportui) | Creates a port and obtains configuration information by displaying a dialog box. |
| [**ConfigurePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-configureportui) | Configures a previously added port. |
| [**DeletePortUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-deleteportui) | Deletes a port. |
| [**InitializePrintMonitorUI**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-initializeprintmonitorui) | Initializes the port monitor UI DLL. |
