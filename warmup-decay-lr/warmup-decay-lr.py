def warmup_decay_schedule(base_lr, warmup_steps, total_steps, current_step):
    """
    Compute the learning rate at a given step using warmup + linear decay.
    """
    # Write code here
    if base_lr > 0 and warmup_steps >=0 and total_steps > warmup_steps and 0 <= current_step <= total_steps:
        if current_step < warmup_steps:
            lr = base_lr * current_step/warmup_steps
        else:
            lr = base_lr * ((total_steps - current_step)/(total_steps - warmup_steps))
        return float(lr)
    else:
        return float(0)