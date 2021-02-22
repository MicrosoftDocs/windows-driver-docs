---
title: Trace Tree Pane Actions
description: Trace Tree Pane Actions
keywords:
- Static Driver Verifier Report WDK , Trace Tree pane
- Trace Tree pane WDK Static Driver Verifier
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Trace Tree Pane Actions

You can perform the following actions in the **Trace Tree** pane:

- Step through the trace
- Expand and collapse nodes

## Step through the trace

The easiest way to step through the trace is by using the arrow keys on your keyboard. The following table describes the action of each arrow key in the **Trace Tree** pane.

|Key|Action|
|----|----|
|DOWN ARROW|Steps down one line. This action skips code that is within collapsed nodes.|
|UP ARROW|Steps up one line. This action skips code that is within collapsed nodes.|
|RIGHT ARROW|Expands a collapsed node.|
|LEFT ARROW|Collapses an expanded node.|

As you step through the source code elements in the **Trace Tree** pane, SDV automatically moves the cursor in the [Source Code pane](source-code-pane.md) to the line of source code that contains the element in the **Trace Tree** pane and displays the associated Boolean expressions in the [State pane](state-pane.md).

## Expand and collapse nodes

Use either of the following methods to expand and collapse nodes in the **Trace Tree** pane:

- To expand or collapse nodes selectively:
  - Use the arrow keys on the keyboard, as described in the preceding table.
  - Click the PLUS SIGN (+) to expand a node or click the MINUS SIGN (-) to collapse a node.
- To expand or collapse all of the nodes in the **Trace Tree** pane, open the **Trace Tree** menu and select **Collapse** (collapse all nodes), **Expand** (expand all nodes), or **Intelligent Expand**. **Intelligent Expand** uses a heuristic to expand the relevant elements of the source code and collapse the less relevant elements. **Intelligent Expand** is the default view.

> [!NOTE]
> When you step through the trace, be aware of all collapsed nodes. The DOWN ARROW key skips all code that is within a collapsed node.
