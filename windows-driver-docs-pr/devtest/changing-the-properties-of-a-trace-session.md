---
title: Changing the Properties of a Trace Session
description: Changing the Properties of a Trace Session
ms.assetid: 6a3522c5-d59b-423b-8d8d-5df9ac3be7cc
keywords:
- trace sessions WDK , properties
- properties WDK TraceView
- changeable properties WDK TraceView
- displaying trace session properties
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





