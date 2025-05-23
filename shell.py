from shell_cmd import Cmd

class Shell:
    def __init__(self, suppress_printing: bool=False) -> None:
        self.suppress_printing = suppress_printing
    
    def echo(self, *args: str) -> Cmd:
        return Cmd("echo", list(args), suppress_printing=self.suppress_printing)
    
    def printf(self, *args: str) -> Cmd:
        return Cmd("printf", list(args), suppress_printing=self.suppress_printing)
    
    def yes(self, *args: str) -> Cmd:
        return Cmd("yes", list(args), suppress_printing=self.suppress_printing)
    
    def tee(self, *args: str) -> Cmd:
        return Cmd("tee", list(args), suppress_printing=self.suppress_printing)
    
    def pwd(self, *args: str) -> Cmd:
        return Cmd("pwd", list(args), suppress_printing=self.suppress_printing)
    
    def basename(self, *args: str) -> Cmd:
        return Cmd("basename", list(args), suppress_printing=self.suppress_printing)
    
    def dirname(self, *args: str) -> Cmd:
        return Cmd("dirname", list(args), suppress_printing=self.suppress_printing)
    
    def date(self, *args: str) -> Cmd:
        return Cmd("date", list(args), suppress_printing=self.suppress_printing)
    
    def uptime(self, *args: str) -> Cmd:
        return Cmd("uptime", list(args), suppress_printing=self.suppress_printing)
    
    def whoami(self, *args: str) -> Cmd:
        return Cmd("whoami", list(args), suppress_printing=self.suppress_printing)
    
    def id(self, *args: str) -> Cmd:
        return Cmd("id", list(args), suppress_printing=self.suppress_printing)
    
    def groups(self, *args: str) -> Cmd:
        return Cmd("groups", list(args), suppress_printing=self.suppress_printing)
    
    def env(self, *args: str) -> Cmd:
        return Cmd("env", list(args), suppress_printing=self.suppress_printing)
    
    def printenv(self, *args: str) -> Cmd:
        return Cmd("printenv", list(args), suppress_printing=self.suppress_printing)
    
    def nice(self, *args: str) -> Cmd:
        return Cmd("nice", list(args), suppress_printing=self.suppress_printing)
    
    def nohup(self, *args: str) -> Cmd:
        return Cmd("nohup", list(args), suppress_printing=self.suppress_printing)
    
    def sleep(self, *args: str) -> Cmd:
        return Cmd("sleep", list(args), suppress_printing=self.suppress_printing)
    
    def timeout(self, *args: str) -> Cmd:
        return Cmd("timeout", list(args), suppress_printing=self.suppress_printing)
        
    def wc(self, *args: str) -> Cmd:
        return Cmd("wc", list(args), suppress_printing=self.suppress_printing)
    
    def tac(self, *args: str) -> Cmd:
        return Cmd("tac", list(args), suppress_printing=self.suppress_printing)
    
    def cut(self, *args: str) -> Cmd:
        return Cmd("cut", list(args), suppress_printing=self.suppress_printing)
    
    def paste(self, *args: str) -> Cmd:
        return Cmd("paste", list(args), suppress_printing=self.suppress_printing)
    
    def head(self, *args: str) -> Cmd:
        return Cmd("head", list(args), suppress_printing=self.suppress_printing)
    
    def tail(self, *args: str) -> Cmd:
        return Cmd("tail", list(args), suppress_printing=self.suppress_printing)
    
    def sort(self, *args: str) -> Cmd:
        return Cmd("sort", list(args), suppress_printing=self.suppress_printing)
    
    def split(self, *args: str) -> Cmd:
        return Cmd("split", list(args), suppress_printing=self.suppress_printing)
    
    def uniq(self, *args: str) -> Cmd:
        return Cmd("uniq", list(args), suppress_printing=self.suppress_printing)
    
    def tr(self, *args: str) -> Cmd:
        return Cmd("tr", list(args), suppress_printing=self.suppress_printing)
    
    def cksum(self, *args: str) -> Cmd:
        return Cmd("cksum", list(args), suppress_printing=self.suppress_printing)
    
    def md5sum(self, *args: str) -> Cmd:
        return Cmd("md5sum", list(args), suppress_printing=self.suppress_printing)
    
    def sha1sum(self, *args: str) -> Cmd:
        return Cmd("sha1sum", list(args), suppress_printing=self.suppress_printing)
    
    def sha256sum(self, *args: str) -> Cmd:
        return Cmd("sha256sum", list(args), suppress_printing=self.suppress_printing)
    
    def sha512sum(self, *args: str) -> Cmd:
        return Cmd("sha512sum", list(args), suppress_printing=self.suppress_printing)
    
    def ls(self, *args: str) -> Cmd:
        return Cmd("ls", list(args), suppress_printing=self.suppress_printing)
    
    def cp(self, *args: str) -> Cmd:
        return Cmd("cp", list(args), suppress_printing=self.suppress_printing)
    
    def rm(self, *args: str) -> Cmd:
        return Cmd("rm", list(args), suppress_printing=self.suppress_printing)
    
    def mv(self, *args: str) -> Cmd:
        return Cmd("mv", list(args), suppress_printing=self.suppress_printing)
    
    def mkdir(self, *args: str) -> Cmd:
        return Cmd("mkdir", list(args), suppress_printing=self.suppress_printing)
    
    def rmdir(self, *args: str) -> Cmd:
        return Cmd("rmdir", list(args), suppress_printing=self.suppress_printing)
    
    def touch(self, *args: str) -> Cmd:
        return Cmd("touch", list(args), suppress_printing=self.suppress_printing)
    
    def stat(self, *args: str) -> Cmd:
        return Cmd("stat", list(args), suppress_printing=self.suppress_printing)
    
    def install(self, *args: str) -> Cmd:
        return Cmd("install", list(args), suppress_printing=self.suppress_printing)
    
    def readlink(self, *args: str) -> Cmd:
        return Cmd("readlink", list(args), suppress_printing=self.suppress_printing)
    
    def df(self, *args: str) -> Cmd:
        return Cmd("df", list(args), suppress_printing=self.suppress_printing)
    
    def du(self, *args: str) -> Cmd:
        return Cmd("du", list(args), suppress_printing=self.suppress_printing)
    
    def chmod(self, *args: str) -> Cmd:
        return Cmd("chmod", list(args), suppress_printing=self.suppress_printing)
    
    def chown(self, *args: str) -> Cmd:
        return Cmd("chown", list(args), suppress_printing=self.suppress_printing)
    
    def chgrp(self, *args: str) -> Cmd:
        return Cmd("chgrp", list(args), suppress_printing=self.suppress_printing)
    
    def unmask(self, *args: str) -> Cmd:
        return Cmd("unmask", list(args), suppress_printing=self.suppress_printing)
    
    def uname(self, *args: str) -> Cmd:
        return Cmd("uname", list(args), suppress_printing=self.suppress_printing)
    
    def hostid(self, *args: str) -> Cmd:
        return Cmd("hostid", list(args), suppress_printing=self.suppress_printing)
    
    def nproc(self, *args: str) -> Cmd:
        return Cmd("nproc", list(args), suppress_printing=self.suppress_printing)
    
    def arch(self, *args: str) -> Cmd:
        return Cmd("arch", list(args), suppress_printing=self.suppress_printing)
    
    def kill(self, *args: str) -> Cmd:
        return Cmd("kill", list(args), suppress_printing=self.suppress_printing)
    
    def killall(self, *args: str) -> Cmd:
        return Cmd("killall", list(args), suppress_printing=self.suppress_printing)
    
    def chcon(self, *args: str) -> Cmd:
        return Cmd("chcon", list(args), suppress_printing=self.suppress_printing)
    
    def runcon(self, *args: str) -> Cmd:
        return Cmd("runcon", list(args), suppress_printing=self.suppress_printing)
    
    def tar(self, *args: str) -> Cmd:
        return Cmd("tar", list(args), suppress_printing=self.suppress_printing)
    
    def gzip(self, *args: str) -> Cmd:
        return Cmd("gzip", list(args), suppress_printing=self.suppress_printing)
    
    def bzip2(self, *args: str) -> Cmd:
        return Cmd("bzip2", list(args), suppress_printing=self.suppress_printing)
    
    def xz(self, *args: str) -> Cmd:
        return Cmd("xz", list(args), suppress_printing=self.suppress_printing)
    
    def wget(self, *args: str) -> Cmd:
        return Cmd("wget", list(args), suppress_printing=self.suppress_printing)
    
    def curl(self, *args: str) -> Cmd:
        return Cmd("curl", list(args), suppress_printing=self.suppress_printing)
    
    def inetutils(self, *args: str) -> Cmd:
        return Cmd("inetutils", list(args), suppress_printing=self.suppress_printing)
    
    def sed(self, *args: str) -> Cmd:
        return Cmd("sed", list(args), suppress_printing=self.suppress_printing)
    
    def awk(self, *args: str) -> Cmd:
        return Cmd("awk", list(args), suppress_printing=self.suppress_printing)
    
    def grep(self, *args: str) -> Cmd:
        return Cmd("grep", list(args), suppress_printing=self.suppress_printing)

    def find(self, *args: str) -> Cmd:
        return Cmd("find", list(args), suppress_printing=self.suppress_printing)

    def locate(self, *args: str) -> Cmd:
        return Cmd("locate", list(args), suppress_printing=self.suppress_printing)

    def xargs(self, *args: str) -> Cmd:
        return Cmd("xargs", list(args), suppress_printing=self.suppress_printing)

    def dd(self, *args: str) -> Cmd:
        return Cmd("dd", list(args), suppress_printing=self.suppress_printing)

    def dmesg(self, *args: str) -> Cmd:
        return Cmd("dmesg", list(args), suppress_printing=self.suppress_printing)
    
    def false(self, *args: str) -> Cmd:
        return Cmd("false", list(args), suppress_printing=self.suppress_printing)
    
    def hostname(self, *args: str) -> Cmd:
        return Cmd("hostname", list(args), suppress_printing=self.suppress_printing)
    
    def ln(self, *args: str) -> Cmd:
        return Cmd("ln", list(args), suppress_printing=self.suppress_printing)
    
    def login(self, *args: str) -> Cmd:
        return Cmd("login", list(args), suppress_printing=self.suppress_printing)
    
    def mknod(self, *args: str) -> Cmd:
        return Cmd("mknod", list(args), suppress_printing=self.suppress_printing)
    
    def more(self, *args: str) -> Cmd:
        return Cmd("more", list(args), suppress_printing=self.suppress_printing)
    
    def less(self, *args: str) -> Cmd:
        return Cmd("less", list(args), suppress_printing=self.suppress_printing)
    
    def mount(self, *args: str) -> Cmd:
        return Cmd("mount", list(args), suppress_printing=self.suppress_printing)
    
    def ps(self, *args: str) -> Cmd:
        return Cmd("ps", list(args), suppress_printing=self.suppress_printing)
    
    def sh(self, *args: str) -> Cmd:
        return Cmd("sh", list(args), suppress_printing=self.suppress_printing)

    def stty(self, *args: str) -> Cmd:
        return Cmd("stty", list(args), suppress_printing=self.suppress_printing)
    
    def su(self, *args: str) -> Cmd:
        return Cmd("su", list(args), suppress_printing=self.suppress_printing)
    
    def sudo(self, *args: str) -> Cmd:
        return Cmd("sudo", list(args), suppress_printing=self.suppress_printing)

    def sync(self, *args: str) -> Cmd:
        return Cmd("sync", list(args), suppress_printing=self.suppress_printing)
    
    def umount(self, *args: str) -> Cmd:
        return Cmd("umount", list(args), suppress_printing=self.suppress_printing)
    
    def clear(self, *args: str) -> Cmd:
        return Cmd("clear", list(args), suppress_printing=self.suppress_printing)

    def bash(self, *args: str) -> Cmd:
        return Cmd("bash", list(args), suppress_printing=self.suppress_printing)
    
    def true(self, *args: str) -> Cmd:
        return Cmd("true", list(args), suppress_printing=self.suppress_printing)
    
    def expr(self, *args: str) -> Cmd:
        return Cmd("expr", list(args), suppress_printing=self.suppress_printing)
    
    def test(self, *args: str) -> Cmd:
        return Cmd("test", list(args), suppress_printing=self.suppress_printing)

    def systemctl(self, *args: str) -> Cmd:
        return Cmd("systemctl", list(args), suppress_printing=self.suppress_printing)

    def systemd_analyze(self, *args: str) -> Cmd:
        return Cmd("systemd-analyze", list(args), suppress_printing=self.suppress_printing)

    def systemd_ask_password(self, *args: str) -> Cmd:
        return Cmd("systemd-ask-password", list(args), suppress_printing=self.suppress_printing)

    def systemd_cat(self, *args: str) -> Cmd:
        return Cmd("systemd-cat", list(args), suppress_printing=self.suppress_printing)

    def systemd_cgls(self, *args: str) -> Cmd:
        return Cmd("systemd-cgls", list(args), suppress_printing=self.suppress_printing)

    def systemd_cgtop(self, *args: str) -> Cmd:
        return Cmd("systemd-cgtop", list(args), suppress_printing=self.suppress_printing)

    def systemd_creds(self, *args: str) -> Cmd:
        return Cmd("systemd-creds", list(args), suppress_printing=self.suppress_printing)

    def systemd_cryptenroll(self, *args: str) -> Cmd:
        return Cmd("systemd-cryptenroll", list(args), suppress_printing=self.suppress_printing)

    def systemd_cryptsetup(self, *args: str) -> Cmd:
        return Cmd("systemd-cryptsetup", list(args), suppress_printing=self.suppress_printing)

    def systemd_delta(self, *args: str) -> Cmd:
        return Cmd("systemd-delta", list(args), suppress_printing=self.suppress_printing)

    def systemd_detect_virt(self, *args: str) -> Cmd:
        return Cmd("systemd-detect-virt", list(args), suppress_printing=self.suppress_printing)

    def systemd_dissect(self, *args: str) -> Cmd:
        return Cmd("systemd-dissect", list(args), suppress_printing=self.suppress_printing)

    def systemd_escape(self, *args: str) -> Cmd:
        return Cmd("systemd-escape", list(args), suppress_printing=self.suppress_printing)

    def systemd_firstboot(self, *args: str) -> Cmd:
        return Cmd("systemd-firstboot", list(args), suppress_printing=self.suppress_printing)

    def systemd_hwdb(self, *args: str) -> Cmd:
        return Cmd("systemd-hwdb", list(args), suppress_printing=self.suppress_printing)

    def systemd_id128(self, *args: str) -> Cmd:
        return Cmd("systemd-id128", list(args), suppress_printing=self.suppress_printing)

    def systemd_inhibit(self, *args: str) -> Cmd:
        return Cmd("systemd-inhibit", list(args), suppress_printing=self.suppress_printing)

    def systemd_machine_id_setup(self, *args: str) -> Cmd:
        return Cmd("systemd-machine-id-setup", list(args), suppress_printing=self.suppress_printing)

    def systemd_mount(self, *args: str) -> Cmd:
        return Cmd("systemd-mount", list(args), suppress_printing=self.suppress_printing)

    def systemd_notify(self, *args: str) -> Cmd:
        return Cmd("systemd-notify", list(args), suppress_printing=self.suppress_printing)

    def systemd_path(self, *args: str) -> Cmd:
        return Cmd("systemd-path", list(args), suppress_printing=self.suppress_printing)

    def systemd_repart(self, *args: str) -> Cmd:
        return Cmd("systemd-repart", list(args), suppress_printing=self.suppress_printing)

    def systemd_run(self, *args: str) -> Cmd:
        return Cmd("systemd-run", list(args), suppress_printing=self.suppress_printing)

    def systemd_socket_activate(self, *args: str) -> Cmd:
        return Cmd("systemd-socket-activate", list(args), suppress_printing=self.suppress_printing)

    def systemd_stdio_bridge(self, *args: str) -> Cmd:
        return Cmd("systemd-stdio-bridge", list(args), suppress_printing=self.suppress_printing)

    def systemd_sysext(self, *args: str) -> Cmd:
        return Cmd("systemd-sysext", list(args), suppress_printing=self.suppress_printing)

    def systemd_sysusers(self, *args: str) -> Cmd:
        return Cmd("systemd-sysusers", list(args), suppress_printing=self.suppress_printing)

    def systemd_tmpfiles(self, *args: str) -> Cmd:
        return Cmd("systemd-tmpfiles", list(args), suppress_printing=self.suppress_printing)

    def systemd_tty_ask_password_agent(self, *args: str) -> Cmd:
        return Cmd("systemd-tty-ask-password-agent", list(args), suppress_printing=self.suppress_printing)

    def systemd_umount(self, *args: str) -> Cmd:
        return Cmd("systemd-umount", list(args), suppress_printing=self.suppress_printing)

    def systemd_vpick(self, *args: str) -> Cmd:
        return Cmd("systemd-vpick", list(args), suppress_printing=self.suppress_printing)
    
    def pacat(self, *args: str) -> Cmd:
        return Cmd("pacat", list(args), suppress_printing=self.suppress_printing)

    def pacmd(self, *args: str) -> Cmd:
        return Cmd("pacmd", list(args), suppress_printing=self.suppress_printing)

    def pactl(self, *args: str) -> Cmd:
        return Cmd("pactl", list(args), suppress_printing=self.suppress_printing)

    def padsp(self, *args: str) -> Cmd:
        return Cmd("padsp", list(args), suppress_printing=self.suppress_printing)

    def paplay(self, *args: str) -> Cmd:
        return Cmd("paplay", list(args), suppress_printing=self.suppress_printing)

    def parec(self, *args: str) -> Cmd:
        return Cmd("parec", list(args), suppress_printing=self.suppress_printing)

    def parecord(self, *args: str) -> Cmd:
        return Cmd("parecord", list(args), suppress_printing=self.suppress_printing)

    def pasuspender(self, *args: str) -> Cmd:
        return Cmd("pasuspender", list(args), suppress_printing=self.suppress_printing)

    def pavucontrol(self, *args: str) -> Cmd:
        return Cmd("pavucontrol", list(args), suppress_printing=self.suppress_printing)

    def pipewire(self, *args: str) -> Cmd:
        return Cmd("pipewire", list(args), suppress_printing=self.suppress_printing)

    def pipewire_aes67(self, *args: str) -> Cmd:
        return Cmd("pipewire-aes67", list(args), suppress_printing=self.suppress_printing)

    def pipewire_avb(self, *args: str) -> Cmd:
        return Cmd("pipewire-avb", list(args), suppress_printing=self.suppress_printing)

    def pipewire_pulse(self, *args: str) -> Cmd:
        return Cmd("pipewire-pulse", list(args), suppress_printing=self.suppress_printing)

    def pipewire_vulkan(self, *args: str) -> Cmd:
        return Cmd("pipewire-vulkan", list(args), suppress_printing=self.suppress_printing)

    def pw_cat(self, *args: str) -> Cmd:
        return Cmd("pw-cat", list(args), suppress_printing=self.suppress_printing)

    def pw_cli(self, *args: str) -> Cmd:
        return Cmd("pw-cli", list(args), suppress_printing=self.suppress_printing)

    def pw_config(self, *args: str) -> Cmd:
        return Cmd("pw-config", list(args), suppress_printing=self.suppress_printing)

    def pw_container(self, *args: str) -> Cmd:
        return Cmd("pw-container", list(args), suppress_printing=self.suppress_printing)

    def pw_dot(self, *args: str) -> Cmd:
        return Cmd("pw-dot", list(args), suppress_printing=self.suppress_printing)

    def pw_dsdplay(self, *args: str) -> Cmd:
        return Cmd("pw-dsdplay", list(args), suppress_printing=self.suppress_printing)

    def pw_dump(self, *args: str) -> Cmd:
        return Cmd("pw-dump", list(args), suppress_printing=self.suppress_printing)

    def pw_encplay(self, *args: str) -> Cmd:
        return Cmd("pw-encplay", list(args), suppress_printing=self.suppress_printing)

    def pw_link(self, *args: str) -> Cmd:
        return Cmd("pw-link", list(args), suppress_printing=self.suppress_printing)

    def pw_loopback(self, *args: str) -> Cmd:
        return Cmd("pw-loopback", list(args), suppress_printing=self.suppress_printing)

    def pw_metadata(self, *args: str) -> Cmd:
        return Cmd("pw-metadata", list(args), suppress_printing=self.suppress_printing)

    def pw_mididump(self, *args: str) -> Cmd:
        return Cmd("pw-mididump", list(args), suppress_printing=self.suppress_printing)

    def pw_midiplay(self, *args: str) -> Cmd:
        return Cmd("pw-midiplay", list(args), suppress_printing=self.suppress_printing)

    def pw_midirecord(self, *args: str) -> Cmd:
        return Cmd("pw-midirecord", list(args), suppress_printing=self.suppress_printing)

    def pw_mon(self, *args: str) -> Cmd:
        return Cmd("pw-mon", list(args), suppress_printing=self.suppress_printing)

    def pw_play(self, *args: str) -> Cmd:
        return Cmd("pw-play", list(args), suppress_printing=self.suppress_printing)

    def pw_profiler(self, *args: str) -> Cmd:
        return Cmd("pw-profiler", list(args), suppress_printing=self.suppress_printing)

    def pw_record(self, *args: str) -> Cmd:
        return Cmd("pw-record", list(args), suppress_printing=self.suppress_printing)

    def pw_reserve(self, *args: str) -> Cmd:
        return Cmd("pw-reserve", list(args), suppress_printing=self.suppress_printing)

    def pw_top(self, *args: str) -> Cmd:
        return Cmd("pw-top", list(args), suppress_printing=self.suppress_printing)

    def pw_v4l2(self, *args: str) -> Cmd:
        return Cmd("pw-v4l2", list(args), suppress_printing=self.suppress_printing)

    def wpctl(self, *args: str) -> Cmd:
        return Cmd("wpctl", list(args), suppress_printing=self.suppress_printing)

    def wpexec(self, *args: str) -> Cmd:
        return Cmd("wpexec", list(args), suppress_printing=self.suppress_printing)

    def wireplumber(self, *args: str) -> Cmd:
        return Cmd("wireplumber", list(args), suppress_printing=self.suppress_printing)
    
    def xinit(self, *args: str) -> Cmd:
        return Cmd("xinit", list(args), suppress_printing=self.suppress_printing)

    def Xorg(self, *args: str) -> Cmd:
        return Cmd("Xorg", list(args), suppress_printing=self.suppress_printing)

    def xset(self, *args: str) -> Cmd:
        return Cmd("xset", list(args), suppress_printing=self.suppress_printing)

    def xrdb(self, *args: str) -> Cmd:
        return Cmd("xrdb", list(args), suppress_printing=self.suppress_printing)

    def xrandr(self, *args: str) -> Cmd:
        return Cmd("xrandr", list(args), suppress_printing=self.suppress_printing)

    def xmessage(self, *args: str) -> Cmd:
        return Cmd("xmessage", list(args), suppress_printing=self.suppress_printing)

    def xmodmap(self, *args: str) -> Cmd:
        return Cmd("xmodmap", list(args), suppress_printing=self.suppress_printing)

    def xprop(self, *args: str) -> Cmd:
        return Cmd("xprop", list(args), suppress_printing=self.suppress_printing)

    def xterm(self, *args: str) -> Cmd:
        return Cmd("xterm", list(args), suppress_printing=self.suppress_printing)

    def xauth(self, *args: str) -> Cmd:
        return Cmd("xauth", list(args), suppress_printing=self.suppress_printing)

    def xhost(self, *args: str) -> Cmd:
        return Cmd("xhost", list(args), suppress_printing=self.suppress_printing)

    def xinput(self, *args: str) -> Cmd:
        return Cmd("xinput", list(args), suppress_printing=self.suppress_printing)

    def xsetroot(self, *args: str) -> Cmd:
        return Cmd("xsetroot", list(args), suppress_printing=self.suppress_printing)

    def xev(self, *args: str) -> Cmd:
        return Cmd("xev", list(args), suppress_printing=self.suppress_printing)

    def xdpyinfo(self, *args: str) -> Cmd:
        return Cmd("xdpyinfo", list(args), suppress_printing=self.suppress_printing)

    def xlsclients(self, *args: str) -> Cmd:
        return Cmd("xlsclients", list(args), suppress_printing=self.suppress_printing)

    def xfce4_power_manager(self, *args: str) -> Cmd:
        return Cmd("xfce4-power-manager", list(args), suppress_printing=self.suppress_printing)

    def xfce4_power_manager_settings(self, *args: str) -> Cmd:
        return Cmd("xfce4-power-manager-settings", list(args), suppress_printing=self.suppress_printing)

    def upower(self, *args: str) -> Cmd:
        return Cmd("upower", list(args), suppress_printing=self.suppress_printing)

    def acpi(self, *args: str) -> Cmd:
        return Cmd("acpi", list(args), suppress_printing=self.suppress_printing)

    def systemd_ac_power(self, *args: str) -> Cmd:
        return Cmd("systemd-ac-power", list(args), suppress_printing=self.suppress_printing)

    def cpupower(self, *args: str) -> Cmd:
        return Cmd("cpupower", list(args), suppress_printing=self.suppress_printing)

    def powertop(self, *args: str) -> Cmd:
        return Cmd("powertop", list(args), suppress_printing=self.suppress_printing)

    def tlp(self, *args: str) -> Cmd:
        return Cmd("tlp", list(args), suppress_printing=self.suppress_printing)

    def rpm(self, *args: str) -> Cmd:
        return Cmd("rpm", list(args), suppress_printing=self.suppress_printing)

    def rpmbuild(self, *args: str) -> Cmd:
        return Cmd("rpmbuild", list(args), suppress_printing=self.suppress_printing)

    def rpm2cpio(self, *args: str) -> Cmd:
        return Cmd("rpm2cpio", list(args), suppress_printing=self.suppress_printing)

    def rpm2archive(self, *args: str) -> Cmd:
        return Cmd("rpm2archive", list(args), suppress_printing=self.suppress_printing)

    def rpmquery(self, *args: str) -> Cmd:
        return Cmd("rpmquery", list(args), suppress_printing=self.suppress_printing)

    def rpmverify(self, *args: str) -> Cmd:
        return Cmd("rpmverify", list(args), suppress_printing=self.suppress_printing)

    def rpmkeys(self, *args: str) -> Cmd:
        return Cmd("rpmkeys", list(args), suppress_printing=self.suppress_printing)

    def rpmsign(self, *args: str) -> Cmd:
        return Cmd("rpmsign", list(args), suppress_printing=self.suppress_printing)

    def rpmspec(self, *args: str) -> Cmd:
        return Cmd("rpmspec", list(args), suppress_printing=self.suppress_printing)

    def rpmdb(self, *args: str) -> Cmd:
        return Cmd("rpmdb", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_setuptree(self, *args: str) -> Cmd:
        return Cmd("rpmdev-setuptree", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_newspectool(self, *args: str) -> Cmd:
        return Cmd("rpmdev-spectool", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_checksig(self, *args: str) -> Cmd:
        return Cmd("rpmdev-checksig", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_diff(self, *args: str) -> Cmd:
        return Cmd("rpmdev-diff", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_packager(self, *args: str) -> Cmd:
        return Cmd("rpmdev-packager", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_bumpspec(self, *args: str) -> Cmd:
        return Cmd("rpmdev-bumpspec", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_vercmp(self, *args: str) -> Cmd:
        return Cmd("rpmdev-vercmp", list(args), suppress_printing=self.suppress_printing)

    def rpmgraph(self, *args: str) -> Cmd:
        return Cmd("rpmgraph", list(args), suppress_printing=self.suppress_printing)

    def rpmqpack(self, *args: str) -> Cmd:
        return Cmd("rpmqpack", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_md5(self, *args: str) -> Cmd:
        return Cmd("rpmdev-md5", list(args), suppress_printing=self.suppress_printing)

    def zypper(self, *args: str) -> Cmd:
        return Cmd("zypper", list(args), suppress_printing=self.suppress_printing)

    def repo2solv(self, *args: str) -> Cmd:
        return Cmd("repo2solv", list(args), suppress_printing=self.suppress_printing)

    def rpmdev_extract(self, *args: str) -> Cmd:
        return Cmd("rpmdev-extract", list(args), suppress_printing=self.suppress_printing)
    
    def ip(self, *args: str) -> Cmd:
        return Cmd("ip", list(args), suppress_printing=self.suppress_printing)

    def ss(self, *args: str) -> Cmd:
        return Cmd("ss", list(args), suppress_printing=self.suppress_printing)

    def ping(self, *args: str) -> Cmd:
        return Cmd("ping", list(args), suppress_printing=self.suppress_printing)

    def traceroute(self, *args: str) -> Cmd:
        return Cmd("traceroute", list(args), suppress_printing=self.suppress_printing)

    def ssh(self, *args: str) -> Cmd:
        return Cmd("ssh", list(args), suppress_printing=self.suppress_printing)

    def scp(self, *args: str) -> Cmd:
        return Cmd("scp", list(args), suppress_printing=self.suppress_printing)

    def nmap(self, *args: str) -> Cmd:
        return Cmd("nmap", list(args), suppress_printing=self.suppress_printing)

    def netstat(self, *args: str) -> Cmd:
        return Cmd("netstat", list(args), suppress_printing=self.suppress_printing)

    def nmcli(self, *args: str) -> Cmd:
        return Cmd("nmcli", list(args), suppress_printing=self.suppress_printing)

    def lspci(self, *args: str) -> Cmd:
        return Cmd("lspci", list(args), suppress_printing=self.suppress_printing)

    def lsusb(self, *args: str) -> Cmd:
        return Cmd("lsusb", list(args), suppress_printing=self.suppress_printing)

    def lscpu(self, *args: str) -> Cmd:
        return Cmd("lscpu", list(args), suppress_printing=self.suppress_printing)

    def sensors(self, *args: str) -> Cmd:
        return Cmd("sensors", list(args), suppress_printing=self.suppress_printing)

    def lsblk(self, *args: str) -> Cmd:
        return Cmd("lsblk", list(args), suppress_printing=self.suppress_printing)

    def dmidecode(self, *args: str) -> Cmd:
        return Cmd("dmidecode", list(args), suppress_printing=self.suppress_printing)
    
    def gunzip(self, *args: str) -> Cmd:
        return Cmd("gunzip", list(args), suppress_printing=self.suppress_printing)

    def zip(self, *args: str) -> Cmd:
        return Cmd("zip", list(args), suppress_printing=self.suppress_printing)

    def unzip(self, *args: str) -> Cmd:
        return Cmd("unzip", list(args), suppress_printing=self.suppress_printing)

    def zstd(self, *args: str) -> Cmd:
        return Cmd("zstd", list(args), suppress_printing=self.suppress_printing)
    
    def ftp(self, *args: str) -> Cmd:
        return Cmd("ftp", list(args), suppress_printing=self.suppress_printing)

    def passwd(self, *args: str) -> Cmd:
        return Cmd("passwd", list(args), suppress_printing=self.suppress_printing)

    def man(self, *args: str) -> Cmd:
        return Cmd("man", list(args), suppress_printing=self.suppress_printing)

    def whatis(self, *args: str) -> Cmd:
        return Cmd("whatis", list(args), suppress_printing=self.suppress_printing)

    def info(self, *args: str) -> Cmd:
        return Cmd("info", list(args), suppress_printing=self.suppress_printing)

    def apropos(self, *args: str) -> Cmd:
        return Cmd("apropos", list(args), suppress_printing=self.suppress_printing)

    def source(self, *args: str) -> Cmd:
        return Cmd("source", list(args), suppress_printing=self.suppress_printing)

    def lp(self, *args: str) -> Cmd:
        return Cmd("lp", list(args), suppress_printing=self.suppress_printing)

    def lpr(self, *args: str) -> Cmd:
        return Cmd("lpr", list(args), suppress_printing=self.suppress_printing)

    def lpq(self, *args: str) -> Cmd:
        return Cmd("lpq", list(args), suppress_printing=self.suppress_printing)

    def lprm(self, *args: str) -> Cmd:
        return Cmd("lprm", list(args), suppress_printing=self.suppress_printing)

    def lpstat(self, *args: str) -> Cmd:
        return Cmd("lpstat", list(args), suppress_printing=self.suppress_printing)
    
    def gcc(self, *args: str) -> Cmd:
        return Cmd("gcc", list(args), suppress_printing=self.suppress_printing)

    def gpp(self, *args: str) -> Cmd:
        return Cmd("g++", list(args), suppress_printing=self.suppress_printing)

    def make(self, *args: str) -> Cmd:
        return Cmd("make", list(args), suppress_printing=self.suppress_printing)

    def cmake(self, *args: str) -> Cmd:
        return Cmd("cmake", list(args), suppress_printing=self.suppress_printing)

    def gdb(self, *args: str) -> Cmd:
        return Cmd("gdb", list(args), suppress_printing=self.suppress_printing)

    def strace(self, *args: str) -> Cmd:
        return Cmd("strace", list(args), suppress_printing=self.suppress_printing)

    def valgrind(self, *args: str) -> Cmd:
        return Cmd("valgrind", list(args), suppress_printing=self.suppress_printing)

    def mkfs(self, *args: str) -> Cmd:
        return Cmd("mkfs", list(args), suppress_printing=self.suppress_printing)

    def fsck(self, *args: str) -> Cmd:
        return Cmd("fsck", list(args), suppress_printing=self.suppress_printing)

    def blkid(self, *args: str) -> Cmd:
        return Cmd("blkid", list(args), suppress_printing=self.suppress_printing)

    def parted(self, *args: str) -> Cmd:
        return Cmd("parted", list(args), suppress_printing=self.suppress_printing)
    
    def cat(self, *args: str) -> Cmd:
        return Cmd("cat", list(args), suppress_printing=self.suppress_printing)
    
    # run something that not in the list
    def command(self, command: str, *args: str) -> Cmd:
        return Cmd(command, list(args), suppress_printing=self.suppress_printing)