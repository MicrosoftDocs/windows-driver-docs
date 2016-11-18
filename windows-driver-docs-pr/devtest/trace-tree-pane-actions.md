---
title: Trace Tree Pane Actions
description: Trace Tree Pane Actions
ms.assetid: 60ccca37-d264-43dc-a502-3a7c7fe0caef
keywords: ["Static Driver Verifier Report WDK , Trace Tree pane", "Trace Tree pane WDK Static Driver Verifier"]
---

# Trace Tree Pane Actions


You can perform the following actions in the **Trace Tree** pane:

-   **Step through the trace**

    The easiest way to step through the trace is by using the arrow keys on your keyboard. The following table describes the action of each arrow key in the **Trace Tree** pane.

    <table>
    <colgroup>
    <col width="50%" />
    <col width="50%" />
    </colgroup>
    <thead>
    <tr class="header">
    <th align="left">Key</th>
    <th align="left">Action</th>
    </tr>
    </thead>
    <tbody>
    <tr class="odd">
    <td align="left"><p>DOWN ARROW</p></td>
    <td align="left"><p>Steps down one line. This action skips code that is within collapsed nodes.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>UP ARROW</p></td>
    <td align="left"><p>Steps up one line. This action skips code that is within collapsed nodes.</p></td>
    </tr>
    <tr class="odd">
    <td align="left"><p>RIGHT ARROW</p></td>
    <td align="left"><p>Expands a collapsed node.</p></td>
    </tr>
    <tr class="even">
    <td align="left"><p>LEFT ARROW</p></td>
    <td align="left"><p>Collapses an expanded node.</p></td>
    </tr>
    </tbody>
    </table>

     

    As you step through the source code elements in the **Trace Tree** pane, SDV automatically moves the cursor in the [Source Code pane](source-code-pane.md) to the line of source code that contains the element in the **Trace Tree** pane and displays the associated Boolean expressions in the [State pane](state-pane.md).

-   **Expand and collapse nodes**

    Use either of the following methods to expand and collapse nodes in the **Trace Tree** pane:

    -   To expand or collapse nodes selectively:
        -   Use the arrow keys on the keyboard, as described in the preceding table.
        -   Click the PLUS SIGN (+) to expand a node or click the MINUS SIGN (-) to collapse a node.
    -   To expand or collapse all of the nodes in the **Trace Tree** pane, open the **Trace Tree** menu and select **Collapse** (collapse all nodes), **Expand** (expand all nodes), or **Intelligent Expand**. **Intelligent Expand** uses a heuristic to expand the relevant elements of the source code and collapse the less relevant elements. **Intelligent Expand** is the default view.

### <span id="comments"></span><span id="COMMENTS"></span>Comments

When you step through the trace, be aware of all collapsed nodes. The DOWN ARROW key skips all code that is within a collapsed node.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[devtest\devtest]:%20Trace%20Tree%20Pane%20Actions%20%20RELEASE:%20%2811/17/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




