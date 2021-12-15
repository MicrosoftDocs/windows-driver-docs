---
title: Example 1 Basic Start Command
description: Example 1 Basic Start Command
keywords:
- trace sessions WDK , starting
- start command
- -start command
- starting trace sessions
ms.date: 04/20/2017
---

# Example 1: Basic Start Command


The following command is an example of the simplest command that starts a standard trace session:

```
tracelog -start MyTrace
```

This command starts a session named "MyTrace". The session has the default values for other session properties, including a log file in the default location, C\\LogFile.etl.

If the command did not include a session name, Tracelog would have started the NT Kernel Logger trace session, which is the default.

Because the command does not include a **-guid** parameter, no providers are enabled for the trace session, but you can use a **tracelog -enable** command to add providers to this session after it starts. See [Example 5: Enabling Trace Providers](example-5--enabling-trace-providers.md) for an example of how to use the **-enable** command.
