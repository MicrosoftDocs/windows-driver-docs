---
title: Selecting Flags and Levels
description: Selecting Flags and Levels
ms.assetid: cde1ef3e-ab1b-4725-b18d-8f7704cc9f5a
keywords: ["trace flags WDK", "flags WDK software tracing", "trace levels WDK", "levels WDK software tracing", "trace sessions WDK , flags", "trace sessions WDK , levels"]
---

# Selecting Flags and Levels


The **Tracing Flags and Level Selection** dialog box allows you to select the [trace flags](trace-flags.md) and [trace level](trace-level.md) for each provider in the trace session. The **Tracing Flags and Level Selection** dialog box conveniently displays all of the flags and levels offered by the provider, so that you do not need to remember them.

Alternately, you can set the **Flags** and **Level** values manually in the **Advanced Log Session Options** dialog box. For information, see [Setting Advanced Trace Session Options](setting-advanced-trace-session-options.md).

This section includes:

[Opening the Tracing Flags and Level Selection dialog box](opening-the-tracing-flags-and-level-selection-dialog-box.md)

[Using the Tracing Flags and Level Selection dialog box](using-the-tracing-flags-and-level-selection-dialog-box.md)

### <span id="comments"></span><span id="COMMENTS"></span>Comments

The **Tracing Flags and Level Selection** dialog box is enabled only when TraceView can find a [PDB symbol file](pdb-symbol-files.md) for the provider or when it can find a [trace message control (.tmc) file](trace-message-control-file.md) for the provider in the TMF path (which was specified by using the **Set TMF Search Path** option). Otherwise, the **Set Flags and Level** button that opens the **Tracing Flags and Level Selection** dialog box is disabled. The dialog box is always disabled when you use the **Select TMF Files** option.

If the **Tracing Flags and Level Selection** dialog box is disabled, you can set the trace flags and level for the provider manually in the **Advanced Trace Session Options** dialog box. For instructions, see [Setting Advanced Trace Session Options](setting-advanced-trace-session-options.md).

Flags and levels are properties of the trace provider. Typically, the flags represent increasingly detailed reporting levels and levels represent the severity of the event (information, warning, or error).

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Selecting%20Flags%20and%20Levels%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




