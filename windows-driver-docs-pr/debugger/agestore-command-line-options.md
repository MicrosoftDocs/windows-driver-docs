---
title: AgeStore Command-Line Options
description: The AgeStore command line uses the following syntax. The parameters can be included in any order.
ms.assetid: ae6ad504-a582-45ac-89a1-7e90952948b4
keywords: ["AgeStore Command-Line Options Windows Debugging"]
ms.author: domars
ms.date: 05/23/2017
topic_type:
- apiref
api_name:
- AgeStore Command-Line Options
api_type:
- NA
ms.localizationpriority: medium
---

# AgeStore Command-Line Options


The AgeStore command line uses the following syntax. The parameters can be included in any order.

```console
agestore [PathSpec] -date=Month-Day-Year Options 

agestore [PathSpec] -days=NumberOfDays Options 

agestore [PathSpec] -size=SizeRemaining Options 

agestore [PathSpec] -size Options 

agestore -? 
```

## <span id="Parameters"></span><span id="parameters"></span><span id="PARAMETERS"></span>Parameters


<span id="_______PathSpec______"></span><span id="_______pathspec______"></span><span id="_______PATHSPEC______"></span> *PathSpec*   
Specifies the target directory in which files are to be deleted. If the -s option is used, *PathSpec* specifies the root directory of the target tree in which files are to be deleted. *PathSpec* may be the absolute or relative path of a directory on the local computer, or a UNC path. If *PathSpec* contains spaces, it must be enclosed in quotation marks. If *PathSpec* is omitted, AgeStore uses the current working directory.

<span id="-date_Month-Day-Year"></span><span id="-date_month-day-year"></span><span id="-DATE_MONTH-DAY-YEAR"></span>**-date=**<em>Month-Day-Year</em>  
Specifies the cutoff date for deleting files. All files that were last accessed prior to the specified date will be deleted. The date must be specified in the format Month-Day-Year, with hyphens between the month and day and between the day and the year. Leading zeros in *Month* and *Day* are optional. The year can be specified with two digits or four. Thus you can indicate the date of January 5, 2008 as 01-05-2008 or 1-5-08.

<span id="_______-days_NumberOfDays______"></span><span id="_______-days_numberofdays______"></span><span id="_______-DAYS_NUMBEROFDAYS______"></span> **-days=**<em>NumberOfDays</em>   
Specifies the cutoff date and time for deleting files. All files that were last accessed prior to the specified number of days ago will be deleted. *NumberOfDays* specifies an integer number of 24-hour days. For example, if the specifier -days=3 is used at 6:00 PM on February 17, 2008, all files last accessed prior to 6:00 PM on February 14, 2008 will be deleted.

<span id="_______-size_SizeRemaining______"></span><span id="_______-size_sizeremaining______"></span><span id="_______-SIZE_SIZEREMAINING______"></span> **-size=**<em>SizeRemaining</em>   
Specifies the total size of the files that should remain after the deletion, in bytes. When this switch is used, AgeStore deletes files in the target directory or target tree, beginning with the files accessed least recently, until the total size of the remaining files is less than or equal to *SizeRemaining*. When the **-s** option is used, AgeStore targets an entire directory tree, and *SizeRemaining* specifies the total size of files that should remain in this entire directory tree after deletion.

<span id="_______-size______"></span><span id="_______-SIZE______"></span> **-size**   
Causes AgeStore to list the total size of all files in the target directory or target tree. No files are deleted.

<span id="_______Options______"></span><span id="_______options______"></span><span id="_______OPTIONS______"></span> *Options*   
Any combination of the following options.

<span id="-l"></span><span id="-L"></span>**-l**  
Causes AgeStore not to delete any files, but merely to list all the files that would be deleted if this same command were run without the **-l** option.

<span id="-s"></span><span id="-S"></span>**-s**  
Causes AgeStore to treat the entire directory tree subordinate to *PathSpec* as the target. When the **-s** option is not used, the directory specified by *PathSpec* becomes the target directory in which files will be deleted. When the **-s** option is used, the directory specified by *PathSpec* and all subdirectories under it become the target tree in which files will be deleted.

<span id="-k"></span><span id="-K"></span>**-k**  
Causes AgeStore to keep any empty subdirectories. If this option is not used, AgeStore deletes the target directory if it is completely empty after the command runs. If the **-s** option is used without the **-k** option, all empty directories in the target directory tree will be deleted after AgeStore has completed its file deletion -- even the root directory itself, if it becomes empty. If there are directories in this tree that happen to be already empty before AgeStore runs, AgeStore deletes these directories as well. However, if the AgeStore command results in no file deletion (for example, if the **-size=**<em>SizeRemaining</em> parameter specifies a size larger than the total size of all files in the target tree), empty directories are not deleted. If the **-s** option is not used, empty directories are never deleted, and the **-k** option is ignored.

<span id="-q"></span><span id="-Q"></span>**-q**  
Quiet mode. If this option is not included, AgeStore lists all files as they are deleted.

<span id="-y"></span><span id="-Y"></span>**-y**  
Suppresses the **(y/n)** prompt. If this option is not used, AgeStore prompts you with an "Are you sure?" prompt before deleting any files.

<span id="_______-_______"></span> **-?**   
Displays help text for the AgeStore command line.

### <span id="Additional_Information"></span><span id="additional_information"></span><span id="ADDITIONAL_INFORMATION"></span>Additional Information

For more information about the AgeStore tool, see [Using AgeStore](using-agestore.md).

 

 





