---
title: PNPCPU
description: PNPCPU
ms.assetid: 397283e6-0691-4e55-9507-483bb311b524
keywords: ["driver testing WDK , PNPCPU", "testing drivers WDK , PNPCPU", "testing drivers WDK , logical processors", "testing drivers WDK , ONECPU", "logical processors WDK"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20PNPCPU%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




