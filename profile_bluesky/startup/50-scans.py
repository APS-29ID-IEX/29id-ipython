print(__file__)

# Bluesky plans (scans)

def monitor_mono_energy(num=10, delay=1):
    yield from count([mono_energy], num=num, delay=delay)

def monitor_mono(num=10, delay=1):
    mono_list = [mono_energy, mono_mirror, mono_grt, mono_error_status]
    yield from count(mono_list, num=num, delay=delay)


def watch_mono_for_hours(hours=24):
    for i in range(hours):
        RE.md["sequence"] = "hour " + str(i+1) + " of " + str(hours)
        yield from monitor_mono(num=60*60)
    del RE.md["sequence"]


def watch_APS_for_hours(hours=24):
    for i in range(hours):
        RE.md["sequence"] = "hour " + str(i+1) + " of " + str(hours)
        yield from count([aps_current], num=2*60*60, delay=0.5)
    del RE.md["sequence"]


def __MyMonitor(signals, *, md=None):
    """
    plan: Monitor a list of signals, emit events as they occur

    Parameters
    ----------
    signals : collection
        objects that support the signal interface
    md : dict, optional
        metadata

    Yields
    ------
    msg : Msg
        'kickoff', 'wait', 'complete, 'wait', 'collect' messages

    See Also
    --------
    :func:`bluesky.plans.fly_during`
    """
    yield from open_run(md)
    for signal in signals:
        yield from monitor(signal)
    #for signal in signals:
    #    yield from complete(signal)
    for signal in signals:
        yield from unmonitor(signal)
    yield from close_run()

