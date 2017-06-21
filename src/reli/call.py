import subprocess

def call(cmd, cwd=None, stdout=None, stderr=None):
    # helper for calling external commands
    # command should be of list of strings type
    # returns output and errors
    # raises Exception if exit code if different from 0
    try:
        p = subprocess.Popen(cmd,
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE,
                             cwd=cwd)
        # p.wait() # potentially unstable
        output, errors = p.communicate()
        if p.returncode != 0:
            raise Exception, errors
        return output, errors
    except Exception, e:
        #print output,errors
        raise Exception, "Error while running command '%s': '%s'" % (' '.join(cmd[0:]), str(e))


# call(['ls', '-l'])


