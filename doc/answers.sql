--create three tables related with fk
CREATE TABLE [IF NOT EXISTS] property (
    id INT PRIMARY,
    name VARCHAR(255) UNIQUE NOT NULL
);

CREATE TABLE [IF NOT EXISTS] room (
    id INT PRIMARY,
    name VARCHAR(255) UNIQUE NOT NULL,
    property_id INT NOT NULL

    FOREIGN KEY (property_id) REFERENCES property (id)
);
CREATE INDEX ix_room_property_id ON room (property_id);


CREATE TABLE [IF NOT EXISTS] order (
    id INT PRIMARY,
    price INT NOT NULL,
    create_at TIMESTAMP WITHOUT TIME ZONE DEFAULT timezone('utc' :: TEXT, now()),
    room_id INT NOT NULL

    FOREIGN KEY (room_id) REFERENCES room (id)
);
CREATE INDEX ix_order_room_id ON order (room_id);

-- get the top 10 properties with the most orders in this Feb
SELECT property.name, count(*) as counts
FROM order
JOIN room ON order.room_id = room.id 
JOIN property ON room.property_id = property.id
WHERE create_at >= '2021-02-01'::date
AND create_at < ('2021-02-01'::date + '1 month'::interval)
GROUP BY property.name
ORDER BY counts
LIMIT 10

-- As for performance, I will use EXPLAIN to check the query plan if the designed indexes were used and where was the bottleneck. Consider adding another index to the create_at column as below.
CREATE INDEX ix_order_create_at ON order (create_at);