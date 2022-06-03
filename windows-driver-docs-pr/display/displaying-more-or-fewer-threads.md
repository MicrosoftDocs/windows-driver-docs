---
title: Displaying More or Fewer Threads
description: "GPUView has six different thread viewing levels."
ms.date: 05/10/2022
---

# Displaying More or Fewer Threads  

GPUView has six different thread viewing levels. You can increase or decrease the amount of thread information that GPUView shows on the screen in the main window. The default viewing level is level 2. You can use different mechanisms to adjust thread viewing level. The thread viewing level is located in the status bar with the label Level. You can use the PLUS SIGN (+) or MINUS SIGN (-) key on your keyboard to adjust the thread viewing level. As you press the PLUS SIGN (+) key, the level value increases, and the amount of information on the screen increases. Likewise, as you press the MINUS SIGN(-) key, the level number decreases, and the amount of information on the screen decreases. Also, you can use the numeric keys on your keyboard to directly enter the number of the level you want. The numbers 1 through 6 map directly to the different levels.  

Each level builds upon the last level by providing more information as the level increases. The following table describes each level and the information provided.  

| Level | Information provided                                                                            |
|-------|-------------------------------------------------------------------------------------------------|
| 1     | Shows only the idle threads along with processes that contain video  contexts.                  |
| 2     | Adds any thread that contains a larger number of Profile events in the  current-view time       |
| 3     | Adds any thread that contains a larger amount of execution time during the  current-view time.  |
| 4     | Adds threads that have any Profile events in the current-view time.                             |
| 5     | Adds threads that have any execution time in the current-view time.                             |
| 6     | Shows all process and all threads.                                                              |  

You can use the following syntax with this option:  

```
Gpuview /l 3   
Gpuview -Limit 5  
```

This adjustable thread-viewing functionality comes in handy when you view smaller blocks of time. As you zoom in and out, the number of threads that GPUView displays remains constant. The smaller block of time that you want to analyze might display a number of threads that contain no information. In this situation, you can press PLUS SIGN (+) followed by MINUS SIGN (-) to make GPUView recalculate the display area.   

> [!NOTE]  
> The difference between levels 2 and 3 and levels 4 and 5 is that there is a cutoff point. The difference from level 2 to level 4 is that the cutoff point is 100 functions. If at least 100 functions are called in the current view window, level 2 displays the thread. If fewer than 100 functions are called in the current view window, the thread is not displayed until you view level 4. Likewise, the difference from level 3 to level 5 is that the cutoff point is 10 percent of the interval (current-view area). If the thread runs for at least 10 percent of the interval, level 3 displays the thread. If the thread runs for less than 10 percent of the interval, the thread is not displayed until you view level 5. 
