---
title: Mouse Functionality
description: "The mouse is a primary tool for discovering details about different items within GPUView's main window."
ms.date: 05/10/2022
---

# Mouse Functionality

The mouse is a primary tool for discovering details about different items within GPUView's main window.

## Zoom Functionality  

The most functional way to zoom in GPUView is to select a region of the viewport and then zoom to that selection using CTRL+Z. Pressing the left mouse button and dragging the mouse will create the selection.

## Measuring 

The most convenient way to measure time periods in GPUView is to create a selection. When selecting, the time difference between the start and end of the selection is displayed as the rightmost item in the status bar.

## Hand Mouse Cursor

When the mouse is over a section of the screen that supports some left-click functionality, the mouse cursor will be displayed as a hand cursor. Typical examples are when the mouse is over a Dma Packet in the GPU Hardware Queue or a Queue Packet in the Context CPU Queue.

## Right-click Context Menu

Almost all of the major areas of the GPUView main window support a right-click context menu. One of the key functionalities built on the context-sensitive right-click is the hiding and showing of the clicked object. For instance, if you click on a Process Area, you get a context menu that says "Hide/Show Process X" where X is the process ID. When that option is selected, that process is minimized in the display showing simply its name so that there is some screen real estate that can function for the right-click in order to show the process again.

## Mouse Cursor Tracking

This is an option on GPUView's main menu. If enabled, mouse tracking means that a gray vertical line is drawn at the x-coordinate of the mouse when it is in the viewport area. This helps when viewing content displayed on different threads or aligning objects with regard to the time.
