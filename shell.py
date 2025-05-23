from shell_cmd import Cmd

class Shell:
    def __init__(self) -> None:
        pass
    
    def echo(self, *args: str) -> Cmd:
        return Cmd("echo", list(args))
    
    def printf(self, *args: str) -> Cmd:
        return Cmd("printf", list(args))
    
    def yes(self, *args: str) -> Cmd:
        return Cmd("yes", list(args))
    
    def tee(self, *args: str) -> Cmd:
        return Cmd("tee", list(args))
    
    def pwd(self, *args: str) -> Cmd:
        return Cmd("pwd", list(args))
    
    def basename(self, *args: str) -> Cmd:
        return Cmd("basename", list(args))
    
    def dirname(self, *args: str) -> Cmd:
        return Cmd("dirname", list(args))
    
    def date(self, *args: str) -> Cmd:
        return Cmd("date", list(args))
    
    def uptime(self, *args: str) -> Cmd:
        return Cmd("uptime", list(args))
    
    def whoami(self, *args: str) -> Cmd:
        return Cmd("whoami", list(args))
    
    def id(self, *args: str) -> Cmd:
        return Cmd("id", list(args))
    
    def groups(self, *args: str) -> Cmd:
        return Cmd("groups", list(args))
    
    def env(self, *args: str) -> Cmd:
        return Cmd("env", list(args))
    
    def printenv(self, *args: str) -> Cmd:
        return Cmd("printenv", list(args))
    
    def nice(self, *args: str) -> Cmd:
        return Cmd("nice", list(args))
    
    def nohup(self, *args: str) -> Cmd:
        return Cmd("nohup", list(args))
    
    def sleep(self, *args: str) -> Cmd:
        return Cmd("sleep", list(args))
    
    def timeout(self, *args: str) -> Cmd:
        return Cmd("timeout", list(args))
        
    def wc(self, *args: str) -> Cmd:
        return Cmd("wc", list(args))
    
    def tac(self, *args: str) -> Cmd:
        return Cmd("tac", list(args))
    
    def cut(self, *args: str) -> Cmd:
        return Cmd("cut", list(args))
    
    def paste(self, *args: str) -> Cmd:
        return Cmd("paste", list(args))
    
    def head(self, *args: str) -> Cmd:
        return Cmd("head", list(args))
    
    def tail(self, *args: str) -> Cmd:
        return Cmd("tail", list(args))
    
    def sort(self, *args: str) -> Cmd:
        return Cmd("sort", list(args))
    
    def split(self, *args: str) -> Cmd:
        return Cmd("split", list(args))
    
    def uniq(self, *args: str) -> Cmd:
        return Cmd("uniq", list(args))
    
    def tr(self, *args: str) -> Cmd:
        return Cmd("tr", list(args))
    
    def cksum(self, *args: str) -> Cmd:
        return Cmd("cksum", list(args))
    
    def md5sum(self, *args: str) -> Cmd:
        return Cmd("md5sum", list(args))
    
    def sha1sum(self, *args: str) -> Cmd:
        return Cmd("sha1sum", list(args))
    
    def sha256sum(self, *args: str) -> Cmd:
        return Cmd("sha256sum", list(args))
    
    def sha512sum(self, *args: str) -> Cmd:
        return Cmd("sha512sum", list(args))
    
    def ls(self, *args: str) -> Cmd:
        return Cmd("ls", list(args))
    
    def cp(self, *args: str) -> Cmd:
        return Cmd("cp", list(args))
    
    def rm(self, *args: str) -> Cmd:
        return Cmd("rm", list(args))
    
    def mv(self, *args: str) -> Cmd:
        return Cmd("mv", list(args))
    
    def mkdir(self, *args: str) -> Cmd:
        return Cmd("mkdir", list(args))
    
    def rmdir(self, *args: str) -> Cmd:
        return Cmd("rmdir", list(args))
    
    def touch(self, *args: str) -> Cmd:
        return Cmd("touch", list(args))
    
    def stat(self, *args: str) -> Cmd:
        return Cmd("stat", list(args))
    
    def install(self, *args: str) -> Cmd:
        return Cmd("install", list(args))
    
    def readlink(self, *args: str) -> Cmd:
        return Cmd("readlink", list(args))
    
    def df(self, *args: str) -> Cmd:
        return Cmd("df", list(args))
    
    def du(self, *args: str) -> Cmd:
        return Cmd("du", list(args))
    
    def chmod(self, *args: str) -> Cmd:
        return Cmd("chmod", list(args))
    
    def chown(self, *args: str) -> Cmd:
        return Cmd("chown", list(args))
    
    def chgrp(self, *args: str) -> Cmd:
        return Cmd("chgrp", list(args))
    
    def unmask(self, *args: str) -> Cmd:
        return Cmd("unmask", list(args))
    
    def uname(self, *args: str) -> Cmd:
        return Cmd("uname", list(args))
    
    def hostid(self, *args: str) -> Cmd:
        return Cmd("hostid", list(args))
    
    def nproc(self, *args: str) -> Cmd:
        return Cmd("nproc", list(args))
    
    def arch(self, *args: str) -> Cmd:
        return Cmd("arch", list(args))
    
    def kill(self, *args: str) -> Cmd:
        return Cmd("kill", list(args))
    
    def killall(self, *args: str) -> Cmd:
        return Cmd("killall", list(args))
    
    def chcon(self, *args: str) -> Cmd:
        return Cmd("chcon", list(args))
    
    def runcon(self, *args: str) -> Cmd:
        return Cmd("runcon", list(args))
    
    def tar(self, *args: str) -> Cmd:
        return Cmd("tar", list(args))
    
    def gzip(self, *args: str) -> Cmd:
        return Cmd("gzip", list(args))
    
    def bzip2(self, *args: str) -> Cmd:
        return Cmd("bzip2", list(args))
    
    def xz(self, *args: str) -> Cmd:
        return Cmd("xz", list(args))
    
    def wget(self, *args: str) -> Cmd:
        return Cmd("wget", list(args))
    
    def curl(self, *args: str) -> Cmd:
        return Cmd("curl", list(args))
    
    def inetutils(self, *args: str) -> Cmd:
        return Cmd("inetutils", list(args))
    
    def sed(self, *args: str) -> Cmd:
        return Cmd("sed", list(args))
    
    def awk(self, *args: str) -> Cmd:
        return Cmd("awk", list(args))
    
    def grep(self, *args: str) -> Cmd:
        return Cmd("grep", list(args))

    def find(self, *args: str) -> Cmd:
        return Cmd("find", list(args))

    def locate(self, *args: str) -> Cmd:
        return Cmd("locate", list(args))

    def xargs(self, *args: str) -> Cmd:
        return Cmd("xargs", list(args))

    def dd(self, *args: str) -> Cmd:
        return Cmd("dd", list(args))

    def dmesg(self, *args: str) -> Cmd:
        return Cmd("dmesg", list(args))
    
    def false(self, *args: str) -> Cmd:
        return Cmd("false", list(args))
    
    def hostname(self, *args: str) -> Cmd:
        return Cmd("hostname", list(args))
    
    def ln(self, *args: str) -> Cmd:
        return Cmd("ln", list(args))
    
    def login(self, *args: str) -> Cmd:
        return Cmd("login", list(args))
    
    def mknod(self, *args: str) -> Cmd:
        return Cmd("mknod", list(args))
    
    def more(self, *args: str) -> Cmd:
        return Cmd("more", list(args))
    
    def less(self, *args: str) -> Cmd:
        return Cmd("less", list(args))
    
    def mount(self, *args: str) -> Cmd:
        return Cmd("mount", list(args))
    
    def ps(self, *args: str) -> Cmd:
        return Cmd("ps", list(args))
    
    def sh(self, *args: str) -> Cmd:
        return Cmd("sh", list(args))

    def stty(self, *args: str) -> Cmd:
        return Cmd("stty", list(args))
    
    def su(self, *args: str) -> Cmd:
        return Cmd("su", list(args))
    
    def sudo(self, *args: str) -> Cmd:
        return Cmd("sudo", list(args))

    def sync(self, *args: str) -> Cmd:
        return Cmd("sync", list(args))
    
    def umount(self, *args: str) -> Cmd:
        return Cmd("umount", list(args))
    
    def clear(self, *args: str) -> Cmd:
        return Cmd("clear", list(args))

    def bash(self, *args: str) -> Cmd:
        return Cmd("bash", list(args))
    
    def true(self, *args: str) -> Cmd:
        return Cmd("true", list(args))
    
    def expr(self, *args: str) -> Cmd:
        return Cmd("expr", list(args))
    
    def test(self, *args: str) -> Cmd:
        return Cmd("test", list(args))

    def systemctl(self, *args: str) -> Cmd:
        return Cmd("systemctl", list(args))

    def systemd_analyze(self, *args: str) -> Cmd:
        return Cmd("systemd-analyze", list(args))

    def systemd_ask_password(self, *args: str) -> Cmd:
        return Cmd("systemd-ask-password", list(args))

    def systemd_cat(self, *args: str) -> Cmd:
        return Cmd("systemd-cat", list(args))

    def systemd_cgls(self, *args: str) -> Cmd:
        return Cmd("systemd-cgls", list(args))

    def systemd_cgtop(self, *args: str) -> Cmd:
        return Cmd("systemd-cgtop", list(args))

    def systemd_creds(self, *args: str) -> Cmd:
        return Cmd("systemd-creds", list(args))

    def systemd_cryptenroll(self, *args: str) -> Cmd:
        return Cmd("systemd-cryptenroll", list(args))

    def systemd_cryptsetup(self, *args: str) -> Cmd:
        return Cmd("systemd-cryptsetup", list(args))

    def systemd_delta(self, *args: str) -> Cmd:
        return Cmd("systemd-delta", list(args))

    def systemd_detect_virt(self, *args: str) -> Cmd:
        return Cmd("systemd-detect-virt", list(args))

    def systemd_dissect(self, *args: str) -> Cmd:
        return Cmd("systemd-dissect", list(args))

    def systemd_escape(self, *args: str) -> Cmd:
        return Cmd("systemd-escape", list(args))

    def systemd_firstboot(self, *args: str) -> Cmd:
        return Cmd("systemd-firstboot", list(args))

    def systemd_hwdb(self, *args: str) -> Cmd:
        return Cmd("systemd-hwdb", list(args))

    def systemd_id128(self, *args: str) -> Cmd:
        return Cmd("systemd-id128", list(args))

    def systemd_inhibit(self, *args: str) -> Cmd:
        return Cmd("systemd-inhibit", list(args))

    def systemd_machine_id_setup(self, *args: str) -> Cmd:
        return Cmd("systemd-machine-id-setup", list(args))

    def systemd_mount(self, *args: str) -> Cmd:
        return Cmd("systemd-mount", list(args))

    def systemd_notify(self, *args: str) -> Cmd:
        return Cmd("systemd-notify", list(args))

    def systemd_path(self, *args: str) -> Cmd:
        return Cmd("systemd-path", list(args))

    def systemd_repart(self, *args: str) -> Cmd:
        return Cmd("systemd-repart", list(args))

    def systemd_run(self, *args: str) -> Cmd:
        return Cmd("systemd-run", list(args))

    def systemd_socket_activate(self, *args: str) -> Cmd:
        return Cmd("systemd-socket-activate", list(args))

    def systemd_stdio_bridge(self, *args: str) -> Cmd:
        return Cmd("systemd-stdio-bridge", list(args))

    def systemd_sysext(self, *args: str) -> Cmd:
        return Cmd("systemd-sysext", list(args))

    def systemd_sysusers(self, *args: str) -> Cmd:
        return Cmd("systemd-sysusers", list(args))

    def systemd_tmpfiles(self, *args: str) -> Cmd:
        return Cmd("systemd-tmpfiles", list(args))

    def systemd_tty_ask_password_agent(self, *args: str) -> Cmd:
        return Cmd("systemd-tty-ask-password-agent", list(args))

    def systemd_umount(self, *args: str) -> Cmd:
        return Cmd("systemd-umount", list(args))

    def systemd_vpick(self, *args: str) -> Cmd:
        return Cmd("systemd-vpick", list(args))
    
    def pacat(self, *args: str) -> Cmd:
        return Cmd("pacat", list(args))

    def pacmd(self, *args: str) -> Cmd:
        return Cmd("pacmd", list(args))

    def pactl(self, *args: str) -> Cmd:
        return Cmd("pactl", list(args))

    def padsp(self, *args: str) -> Cmd:
        return Cmd("padsp", list(args))

    def paplay(self, *args: str) -> Cmd:
        return Cmd("paplay", list(args))

    def parec(self, *args: str) -> Cmd:
        return Cmd("parec", list(args))

    def parecord(self, *args: str) -> Cmd:
        return Cmd("parecord", list(args))

    def pasuspender(self, *args: str) -> Cmd:
        return Cmd("pasuspender", list(args))

    def pavucontrol(self, *args: str) -> Cmd:
        return Cmd("pavucontrol", list(args))

    def pipewire(self, *args: str) -> Cmd:
        return Cmd("pipewire", list(args))

    def pipewire_aes67(self, *args: str) -> Cmd:
        return Cmd("pipewire-aes67", list(args))

    def pipewire_avb(self, *args: str) -> Cmd:
        return Cmd("pipewire-avb", list(args))

    def pipewire_pulse(self, *args: str) -> Cmd:
        return Cmd("pipewire-pulse", list(args))

    def pipewire_vulkan(self, *args: str) -> Cmd:
        return Cmd("pipewire-vulkan", list(args))

    def pw_cat(self, *args: str) -> Cmd:
        return Cmd("pw-cat", list(args))

    def pw_cli(self, *args: str) -> Cmd:
        return Cmd("pw-cli", list(args))

    def pw_config(self, *args: str) -> Cmd:
        return Cmd("pw-config", list(args))

    def pw_container(self, *args: str) -> Cmd:
        return Cmd("pw-container", list(args))

    def pw_dot(self, *args: str) -> Cmd:
        return Cmd("pw-dot", list(args))

    def pw_dsdplay(self, *args: str) -> Cmd:
        return Cmd("pw-dsdplay", list(args))

    def pw_dump(self, *args: str) -> Cmd:
        return Cmd("pw-dump", list(args))

    def pw_encplay(self, *args: str) -> Cmd:
        return Cmd("pw-encplay", list(args))

    def pw_link(self, *args: str) -> Cmd:
        return Cmd("pw-link", list(args))

    def pw_loopback(self, *args: str) -> Cmd:
        return Cmd("pw-loopback", list(args))

    def pw_metadata(self, *args: str) -> Cmd:
        return Cmd("pw-metadata", list(args))

    def pw_mididump(self, *args: str) -> Cmd:
        return Cmd("pw-mididump", list(args))

    def pw_midiplay(self, *args: str) -> Cmd:
        return Cmd("pw-midiplay", list(args))

    def pw_midirecord(self, *args: str) -> Cmd:
        return Cmd("pw-midirecord", list(args))

    def pw_mon(self, *args: str) -> Cmd:
        return Cmd("pw-mon", list(args))

    def pw_play(self, *args: str) -> Cmd:
        return Cmd("pw-play", list(args))

    def pw_profiler(self, *args: str) -> Cmd:
        return Cmd("pw-profiler", list(args))

    def pw_record(self, *args: str) -> Cmd:
        return Cmd("pw-record", list(args))

    def pw_reserve(self, *args: str) -> Cmd:
        return Cmd("pw-reserve", list(args))

    def pw_top(self, *args: str) -> Cmd:
        return Cmd("pw-top", list(args))

    def pw_v4l2(self, *args: str) -> Cmd:
        return Cmd("pw-v4l2", list(args))

    def wpctl(self, *args: str) -> Cmd:
        return Cmd("wpctl", list(args))

    def wpexec(self, *args: str) -> Cmd:
        return Cmd("wpexec", list(args))

    def wireplumber(self, *args: str) -> Cmd:
        return Cmd("wireplumber", list(args))
    
    def xinit(self, *args: str) -> Cmd:
        return Cmd("xinit", list(args))

    def Xorg(self, *args: str) -> Cmd:
        return Cmd("Xorg", list(args))

    def xset(self, *args: str) -> Cmd:
        return Cmd("xset", list(args))

    def xrdb(self, *args: str) -> Cmd:
        return Cmd("xrdb", list(args))

    def xrandr(self, *args: str) -> Cmd:
        return Cmd("xrandr", list(args))

    def xmessage(self, *args: str) -> Cmd:
        return Cmd("xmessage", list(args))

    def xmodmap(self, *args: str) -> Cmd:
        return Cmd("xmodmap", list(args))

    def xprop(self, *args: str) -> Cmd:
        return Cmd("xprop", list(args))

    def xterm(self, *args: str) -> Cmd:
        return Cmd("xterm", list(args))

    def xauth(self, *args: str) -> Cmd:
        return Cmd("xauth", list(args))

    def xhost(self, *args: str) -> Cmd:
        return Cmd("xhost", list(args))

    def xinput(self, *args: str) -> Cmd:
        return Cmd("xinput", list(args))

    def xsetroot(self, *args: str) -> Cmd:
        return Cmd("xsetroot", list(args))

    def xev(self, *args: str) -> Cmd:
        return Cmd("xev", list(args))

    def xdpyinfo(self, *args: str) -> Cmd:
        return Cmd("xdpyinfo", list(args))

    def xlsclients(self, *args: str) -> Cmd:
        return Cmd("xlsclients", list(args))

    def xfce4_power_manager(self, *args: str) -> Cmd:
        return Cmd("xfce4-power-manager", list(args))

    def xfce4_power_manager_settings(self, *args: str) -> Cmd:
        return Cmd("xfce4-power-manager-settings", list(args))

    def upower(self, *args: str) -> Cmd:
        return Cmd("upower", list(args))

    def acpi(self, *args: str) -> Cmd:
        return Cmd("acpi", list(args))

    def systemd_ac_power(self, *args: str) -> Cmd:
        return Cmd("systemd-ac-power", list(args))

    def cpupower(self, *args: str) -> Cmd:
        return Cmd("cpupower", list(args))

    def powertop(self, *args: str) -> Cmd:
        return Cmd("powertop", list(args))

    def tlp(self, *args: str) -> Cmd:
        return Cmd("tlp", list(args))

    def rpm(self, *args: str) -> Cmd:
        return Cmd("rpm", list(args))

    def rpmbuild(self, *args: str) -> Cmd:
        return Cmd("rpmbuild", list(args))

    def rpm2cpio(self, *args: str) -> Cmd:
        return Cmd("rpm2cpio", list(args))

    def rpm2archive(self, *args: str) -> Cmd:
        return Cmd("rpm2archive", list(args))

    def rpmquery(self, *args: str) -> Cmd:
        return Cmd("rpmquery", list(args))

    def rpmverify(self, *args: str) -> Cmd:
        return Cmd("rpmverify", list(args))

    def rpmkeys(self, *args: str) -> Cmd:
        return Cmd("rpmkeys", list(args))

    def rpmsign(self, *args: str) -> Cmd:
        return Cmd("rpmsign", list(args))

    def rpmspec(self, *args: str) -> Cmd:
        return Cmd("rpmspec", list(args))

    def rpmdb(self, *args: str) -> Cmd:
        return Cmd("rpmdb", list(args))

    def rpmdev_setuptree(self, *args: str) -> Cmd:
        return Cmd("rpmdev-setuptree", list(args))

    def rpmdev_newspectool(self, *args: str) -> Cmd:
        return Cmd("rpmdev-spectool", list(args))

    def rpmdev_checksig(self, *args: str) -> Cmd:
        return Cmd("rpmdev-checksig", list(args))

    def rpmdev_diff(self, *args: str) -> Cmd:
        return Cmd("rpmdev-diff", list(args))

    def rpmdev_packager(self, *args: str) -> Cmd:
        return Cmd("rpmdev-packager", list(args))

    def rpmdev_bumpspec(self, *args: str) -> Cmd:
        return Cmd("rpmdev-bumpspec", list(args))

    def rpmdev_vercmp(self, *args: str) -> Cmd:
        return Cmd("rpmdev-vercmp", list(args))

    def rpmgraph(self, *args: str) -> Cmd:
        return Cmd("rpmgraph", list(args))

    def rpmqpack(self, *args: str) -> Cmd:
        return Cmd("rpmqpack", list(args))

    def rpmdev_md5(self, *args: str) -> Cmd:
        return Cmd("rpmdev-md5", list(args))

    def zypper(self, *args: str) -> Cmd:
        return Cmd("zypper", list(args))

    def repo2solv(self, *args: str) -> Cmd:
        return Cmd("repo2solv", list(args))

    def rpmdev_extract(self, *args: str) -> Cmd:
        return Cmd("rpmdev-extract", list(args))
    
    def ip(self, *args: str) -> Cmd:
        return Cmd("ip", list(args))

    def ss(self, *args: str) -> Cmd:
        return Cmd("ss", list(args))

    def ping(self, *args: str) -> Cmd:
        return Cmd("ping", list(args))

    def traceroute(self, *args: str) -> Cmd:
        return Cmd("traceroute", list(args))

    def ssh(self, *args: str) -> Cmd:
        return Cmd("ssh", list(args))

    def scp(self, *args: str) -> Cmd:
        return Cmd("scp", list(args))

    def nmap(self, *args: str) -> Cmd:
        return Cmd("nmap", list(args))

    def netstat(self, *args: str) -> Cmd:
        return Cmd("netstat", list(args))

    def nmcli(self, *args: str) -> Cmd:
        return Cmd("nmcli", list(args))

    def lspci(self, *args: str) -> Cmd:
        return Cmd("lspci", list(args))

    def lsusb(self, *args: str) -> Cmd:
        return Cmd("lsusb", list(args))

    def lscpu(self, *args: str) -> Cmd:
        return Cmd("lscpu", list(args))

    def sensors(self, *args: str) -> Cmd:
        return Cmd("sensors", list(args))

    def lsblk(self, *args: str) -> Cmd:
        return Cmd("lsblk", list(args))

    def dmidecode(self, *args: str) -> Cmd:
        return Cmd("dmidecode", list(args))
    
    def gunzip(self, *args: str) -> Cmd:
        return Cmd("gunzip", list(args))

    def zip(self, *args: str) -> Cmd:
        return Cmd("zip", list(args))

    def unzip(self, *args: str) -> Cmd:
        return Cmd("unzip", list(args))

    def zstd(self, *args: str) -> Cmd:
        return Cmd("zstd", list(args))
    
    def ftp(self, *args: str) -> Cmd:
        return Cmd("ftp", list(args))

    def passwd(self, *args: str) -> Cmd:
        return Cmd("passwd", list(args))

    def man(self, *args: str) -> Cmd:
        return Cmd("man", list(args))

    def whatis(self, *args: str) -> Cmd:
        return Cmd("whatis", list(args))

    def info(self, *args: str) -> Cmd:
        return Cmd("info", list(args))

    def apropos(self, *args: str) -> Cmd:
        return Cmd("apropos", list(args))

    def source(self, *args: str) -> Cmd:
        return Cmd("source", list(args))

    def lp(self, *args: str) -> Cmd:
        return Cmd("lp", list(args))

    def lpr(self, *args: str) -> Cmd:
        return Cmd("lpr", list(args))

    def lpq(self, *args: str) -> Cmd:
        return Cmd("lpq", list(args))

    def lprm(self, *args: str) -> Cmd:
        return Cmd("lprm", list(args))

    def lpstat(self, *args: str) -> Cmd:
        return Cmd("lpstat", list(args))
    
    def gcc(self, *args: str) -> Cmd:
        return Cmd("gcc", list(args))

    def gpp(self, *args: str) -> Cmd:
        return Cmd("g++", list(args))

    def make(self, *args: str) -> Cmd:
        return Cmd("make", list(args))

    def cmake(self, *args: str) -> Cmd:
        return Cmd("cmake", list(args))

    def gdb(self, *args: str) -> Cmd:
        return Cmd("gdb", list(args))

    def strace(self, *args: str) -> Cmd:
        return Cmd("strace", list(args))

    def valgrind(self, *args: str) -> Cmd:
        return Cmd("valgrind", list(args))

    def mkfs(self, *args: str) -> Cmd:
        return Cmd("mkfs", list(args))

    def fsck(self, *args: str) -> Cmd:
        return Cmd("fsck", list(args))

    def blkid(self, *args: str) -> Cmd:
        return Cmd("blkid", list(args))

    def parted(self, *args: str) -> Cmd:
        return Cmd("parted", list(args))
    
    # run something that not in the list
    def custom_command(self, command: str, *args: str) -> Cmd:
        return Cmd(command, list(args))