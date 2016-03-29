---
title: Debugging Spooler Components
description: Debugging Spooler Components
ms.assetid: ed4dcd29-105c-4562-9741-858cb9542449
keywords: ["debugging spooler components WDK printer", "spooler component debugging WDK print", "trace messages WDK printer"]
---

# Debugging Spooler Components


## <a href="" id="ddk-debugging-spooler-components-gg"></a>


This section provides information about how you can enable debug messages in spooler components. The first part of this section lists the debug variables used in spooler components. You can use these debug variables to cause debug messages originating in spooler components to be displayed. (Note that you must be working with checked builds of these components.)

The second part of this section details the steps need to display trace messages in a spooler component.

**Note**   There are special considerations for [debugging XPSDrv printer drivers](debugging-xpsdrv-printer-drivers.md).

 

### Displaying Trace Messages in a Spooler Component

The following procedure lists the steps necessary for you to be able to see trace messages in checked builds of winspool.drv. The steps for displaying trace messages are similar for other spooler components.

To display trace messages in a spooler component:

1.  Attach a debugger.

2.  Break into the process you want to debug.

3.  Find the debug variable, winspool!ClientDebug.

4.  Set the DBG\_TRACE bit (0x0008) in the low WORD of the winspool!ClientDebug variable.

5.  Click Go.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bprint\print%5D:%20Debugging%20Spooler%20Components%20%20RELEASE:%20%283/29/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




