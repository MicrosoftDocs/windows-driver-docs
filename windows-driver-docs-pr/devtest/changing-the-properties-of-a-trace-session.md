---
title: Changing the Properties of a Trace Session
description: Changing the Properties of a Trace Session
ms.assetid: 6a3522c5-d59b-423b-8d8d-5df9ac3be7cc
keywords: ["trace sessions WDK , properties", "properties WDK TraceView", "changeable properties WDK TraceView", "displaying trace session properties"]
---

# Changing the Properties of a Trace Session


You can change selected properties of a trace session while the session is running. You can also change the [trace flags](trace-flags.md) and [trace level](trace-level.md) properties of a trace provider while the session is running.

### <span id="display_the_properties"></span><span id="DISPLAY_THE_PROPERTIES"></span>Display the Properties

The columns in the [Trace Session List](trace-session-list.md) represent properties of the trace session and its providers.

To display all properties of a trace session and its providers, in the Trace Session List, right-click any column heading. This action displays a shortcut menu that shows all of the available columns. Checked columns are displayed in the Trace Session List and unchecked columns are hidden. To display or hide a column in the Trace Session List, in the shortcut menu, click the column name.

To save your column configuration as the default for future TraceView sessions, right-click any column heading in the Trace Session List, and then click **Save As Default**.

### <span id="find_changeable_properties"></span><span id="FIND_CHANGEABLE_PROPERTIES"></span>Find Changeable Properties

The columns in the [Trace Session List](trace-session-list.md) represent properties of the trace session and its trace providers.

For a running trace session, properties that can be changed while the trace session is running appear available. Properties that can be changed only when the trace session is stopped are dimmed. The properties of trace messages in trace logs cannot be changed.

### <span id="change_a_property"></span><span id="CHANGE_A_PROPERTY"></span>Change a Property

To change the value of a property, click the value, and then type a new value in the field. To save the new value, click in any other cell.

### <span id="set_value"></span><span id="SET_VALUE"></span>SET value

The values in the **Flags** and **Level** columns represent the [trace flags](trace-flags.md) and [trace level](trace-level.md) properties of the trace providers in the trace session. The value in the **Flags** and **Level** column can be a hexadecimal value that represents the actual values or the word "SET".

A value of **SET** indicates that the trace flags and trace level are set in the **Tracing Flags and Level Selection** dialog box. To open the **Tracing Flags and Level Selection** dialog box, click the **SET** value.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Changing%20the%20Properties%20of%20a%20Trace%20Session%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




