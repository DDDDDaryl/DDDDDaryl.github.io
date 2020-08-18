---
title: batch-file-to-set-wireless-hotspot-on-system-boot
date: 2020-08-17 20:10:50
categories:
- techissue
tags:
- Win10
- wireless hotspot
---

> https://stackoverflow.com/questions/29686633/batch-file-to-set-wireless-hotspot-on-system-boot

Since you tagged "autorun", I'll assume this is a windows system.

a [startup script](https://technet.microsoft.com/en-us/library/cc770556.aspx) could look something like:

```
timeout 60
netsh wlan set hostednetwork mode=allow ssid=WLAN_XXXX key=XXXXXXXXXXX
timeout 10
netsh wlan start hostednetwork
```

On windows systems without the availability of the timeout command, you could use ping for the delays as ping waits 1 second between sending packets:

```
ping -n 61 127.0.0.1 > nul
netsh wlan set hostednetwork mode=allow ssid=WLAN_XXXX key=XXXXXXXXXXX
ping -n 11 127.0.0.1 > nul
netsh wlan start hostednetwork
```

The relevant part from linked article about creating startup scripts:

> To assign computer startup scripts
>
> Open the Local Group Policy Editor.
>
> In the console tree, click Scripts (Startup/Shutdown) . The path is Computer Configuration\Windows Settings\Scripts (Startup/Shutdown).
>
> In the results pane, double-click Startup.
>
> In the Startup Properties dialog box, click Add .
>
> In the Add a Script dialog box, do the following: In the Script Name box, type the path to the script, or click Browse to search for the script file in the Netlogon shared folder on the domain controller.
>
> In the Script Parameters box, type any parameters that you want, the same way as you would type them on the command line. For example, if your script includes parameters called //logo (display banner) and //I (interactive mode), type //logo //I.
>
> In the Startup Properties dialog box, specify the options that you want: Startup Scripts for : Lists all the scripts that currently are assigned to the selected Group Policy object (GPO). If you assign multiple scripts, the scripts are processed in the order that you specify. To move a script up in the list, click it and then click Up . To move a script down in the list, click it and then click Down .
>
> Add : Opens the Add a Script dialog box, where you can specify any additional scripts to use.
>
> Edit : Opens the Edit Script dialog box, where you can modify script information, such as name and parameters.
>
> Remove : Removes the selected script from the Startup Scripts list.
>
> Show Files : Displays the script files that are stored in the selected GPO.

**Edit:**

Easier explanation about startup scripts from [this post](https://serverfault.com/questions/116120/need-a-way-to-run-a-script-on-windows-boot-up-prior-to-a-user-logging-in):

> You can use a Group Policy (or the local policy) to assign a startup script; you can configure it in the section *Computer Configuration -> Windows Settings -> Scripts (Startup/Shutdown)*.
>
> You can also use Scheduled Tasks to configure a task to run at computer startup.

---

# 实操

首先，写脚本。

```powershell
ping -n 61 127.0.0.1 > nul
netsh wlan set hostednetwork mode=allow ssid=YYNB2019 key=12345654321
ping -n 11 127.0.0.1 > nul
netsh wlan start hostednetwork
```

最后发现无线网卡并不支持承载网络，无法用命令行启动。