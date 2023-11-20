import redis.clients.jedis.Jedis;

public class RedisDistributedLockExample {

    public static void main(String[] args) {
        // Create a Jedis connection to the Redis server
        try (Jedis jedis = new Jedis("localhost")) {
            // Define the lock key
            String lockKey = "mylock";

            // Try to acquire the lock
            String lockValue = "locked";
            String result = jedis.set(lockKey, lockValue, "NX", "EX", 10);

            if ("OK".equals(result)) {
                // Lock acquired, perform the critical section
                System.out.println("Lock acquired! Performing critical section...");

                // Simulate some work
                Thread.sleep(2000);

                // Release the lock when done
                jedis.del(lockKey);
                System.out.println("Lock released.");
            } else {
                // Lock not acquired, another process holds the lock
                System.out.println("Failed to acquire lock. Another process is performing the critical section.");
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
