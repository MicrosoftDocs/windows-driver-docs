---
title: Process cannot access file Path because it is being used by another process
description: The process cannot access the file path because it is being used by another process.
ms.date: 04/20/2017
---

# The process cannot access the file "&lt;Path&gt;" because it is being used by another process


SDV displays this message when it tries to delete files in response to **staticdv /clean**, **staticdv /clean /force**, or **staticdv /cleanalllibs** commands, but it cannot gain access to the files because they are being accessed by another application. To resolve the problem, close any applications that might be using the files and submit the command again.

