---
title: Find Dialog Box
description: "The Find dialog box helps the user find specific processes or threads in the main window of GPUView."
ms.date: 05/10/2022
---

# Find Dialog Box

The **Find** dialog box helps the user find specific processes or threads in the main window of GPUView. The following diagram is a screen shot of the dialog.  

![find dialog box 1](\Images\find-dialog-box-1.png)

When the dialog is first displayed, the keyboard focus is placed in the **Find what** edit control. The **Find** dialog uses the text that the user enters to find substrings in the Process or Thread names so that when a match is found, it can be scrolled into view. As soon as the user enters text into the **Find what** control, the **Find Next** button is enabled so that searches can be performed. 

The process and thread names are found along the left-hand side of GPUView's main window, as shown with the following screen shot. 

![find dialog box 2](\Images\find-dialog-box-2.png)

Any part of the displayed name can be part of the search. As shown in this diagram, the hexadecimal offsets can be part of the search. If symbols are enabled, the offsets are resolved into the user-friendly names, which helps considerably when performing the searches.  

## Find Next button

This button is linked to the ENTER key. Pressing the button or pressing the ENTER key activates a search for the string in the **Find what** edit control. When a match is found, the dialog scrolls that match into view. If no match is found, the dialog issues the standard system message beep. Note that the search is performed considering the view levels shown in the main window. If the search string matches a process or thread that is not currently displayed at the current view level, the view level is adjusted to show the process or thread. This makes it easier to find hidden threads and processes. 

## Cancel

Terminates the dialog without saving settings.

## Done

Terminates the dialog and saves settings.

## Processes and Threads check boxes

When the search is performed, the process and thread lists are considered only if the corresponding check box is selected.

## Direction

The dialog remembers the current search location. This means that you can search up or down. The default search direction is down.
