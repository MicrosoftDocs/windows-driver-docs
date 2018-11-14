---
title: Using the Help Documentation
description: Using the Help Documentation
ms.assetid: ad826f45-3bad-4e10-811f-26ebf4f06c4d
keywords: ["HTML Help", "searching the Help file", "index of the Help file", "favorites in the Help file", "printing topics from the Help file", "hh.exe", "help file", "help file, overview", "help file, searching"]
ms.author: domars
ms.date: 05/23/2017
ms.localizationpriority: medium
---

# Using the Help Documentation


## <span id="ddk_using_the_help_file_dbg"></span><span id="DDK_USING_THE_HELP_FILE_DBG"></span>


The WinDbg Help documentation that you are reading is the documentation for the Debugging Tools for Windows package.

This documentation uses the viewer that is supplied with Microsoft HTML Help (hh.exe). This viewer provides a table of contents and index and enables you to search through the documentation, mark your favorite or frequently used topics, and print one or more topics.

The following sections in this topic describe the features of and how to use the Help documentation.

### <span id="contents_tab"></span><span id="CONTENTS_TAB"></span>Contents Tab

The **Contents** tab provides an expandable view of the documentation's table of contents.

Click the plus sign (**+**) next to a node or double-click the node's title to expand or contract the table of contents under that node.

### <span id="index_tab"></span><span id="INDEX_TAB"></span>Index Tab

The **Index** tab displays the complete index of terms that are used in this documentation. You can enter the beginning of a term or use the scrollbar to look through this index.

### <span id="search_tab"></span><span id="SEARCH_TAB"></span>Search Tab

In the **Search** tab, you can search for any word or phrase that is contained in the documentation. You can search all text or limit your search to topic titles.

To search for phrases that contain more than one word, enclose the phrase in quotation marks. You can connect multiple words and phrases with the AND, OR, and NOT operators. The default operator is AND.

Note that "AND NOT" is invalid. To search for topics that contain *x* and not *y*, use "*x* NOT *y*". You can also use NEAR in searches.

Wildcard characters are also permitted. Use a question mark (**?**) to represent any single character and an asterisk (**\\***) to represent zero or more characters. However, you cannot use wildcard characters within quoted strings.

All letters and numbers are treated literally, but some symbols are not permitted in searches.

A search returns a list of all topics that match the specified criteria. If you select the **Search previous results** box, you can then search these results for more terms.

### <span id="favorites_tab"></span><span id="FAVORITES_TAB"></span>Favorites Tab

In the **Favorites** tab, you can save the titles of commonly-visited topics. While you are viewing a topic, click the **Favorites** tab and then click the **Add** button.

To rename a page on your favorites list, click its name two times slowly, and retype the name. To view a topic on the Favorites list, double-click its name or click it one time and then click **Display**. To remove a topic from the favorites list, click it one time and then click **Remove**.

### <span id="printing_topics"></span><span id="PRINTING_TOPICS"></span>Printing Topics

To print one or more topics, click a topic in the **Contents** tab, and then click the **Print** button on the toolbar. You will be asked whether you want to print only the selected topic or that topic and all of its subtopics.

You can also print the topic that you are viewing by right-clicking within the view window, and clicking **Print** on the shortcut menu. However, this method does not enable you to print subtopics.

### <span id="searching_within_a_topic"></span><span id="SEARCHING_WITHIN_A_TOPIC"></span>Searching Within a Topic

To search for a text string within the topic that you are viewing, press CTRL+F, or click **Find in this Topic** on the **Edit** menu.

### <span id="accessing_the_help_documentation"></span><span id="ACCESSING_THE_HELP_DOCUMENTATION"></span>Accessing the Help Documentation

To open this Help documentation, do one of the following:

-   Click **Start**, point to **All Programs**, point to **Debugging Tools for Windows**, and then click **Debugging Help**.

-   Open Windows Explorer, locate the Debugger.chm file, and then double-click it.

-   At a command prompt, browse to the folder that contains Debugger.chm and run **hh debugger.chm**.

-   In any Windows debugger, use the [**.hh (Open HTML Help File)**](-hh--open-html-help-file-.md) command.

-   In WinDbg, click **Contents** on the **Help** menu. This command open the Help documentation and opens the **Contents** tab.

-   In WinDbg, click **Index** on the **Help** menu. This command open the Help documentation and opens the **Index** tab.

-   In WinDbg, click **Search** on the **Help** menu. This command opens the Help documentation and opens the **Search** tab.

-   Many dialog boxes in WinDbg have **Help** buttons. Click **Help** to open this documentation and open the relevant page.

 

 





