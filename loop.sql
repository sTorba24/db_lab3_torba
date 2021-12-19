select * from children;
create table childrencopy as select * from children; 
select * from childrencopy;


DO $$
DECLARE
    child_id     	childrencopy.child_id%TYPE;
    child_name   	childrencopy.child_name %TYPE;
BEGIN
    child_id := 100;
    child_name := 'Name';
	
    FOR counter IN 1..5
        LOOP
            INSERT INTO childrencopy(child_id, child_name)
            VALUES (child_id + counter, child_name || counter);
        END LOOP;
END
$$
