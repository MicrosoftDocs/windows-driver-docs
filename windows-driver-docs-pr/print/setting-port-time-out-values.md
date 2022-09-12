---
title: Set port time-out values
description: Provides information about how to set port time-out values.
keywords:
- port management WDK print , time-out values
- time-outs WDK print
- OpenPort
- SetPortTimeOuts
ms.date: 09/08/2022
---

# Set port time-out values

If you are writing a port monitor for a port that has modifiable time-out values, the time-out values should be initialized from within the monitor's [**OpenPort**](/windows-hardware/drivers/ddi/winsplp/nf-winsplp-openport) function. For example the **OpenPort** function in *Localmon.dll*, the [sample port monitor](sample-port-monitor.md), calls the [**SetCommTimeouts**](/windows/win32/api/winbase/nf-winbase-setcommtimeouts) function for this purpose.

Additionally, a port monitor can optionally provide a [**SetPortTimeOuts**](/previous-versions/ff562630(v=vs.85)) function, which can be called by language monitors. The function is called by *Pjlmon.dll*, the [sample language monitor](sample-language-monitor.md). The print spooler does not call **SetPortTimeOuts**.
