import org.junit.Test;

import java.util.logging.Logger;

import static org.junit.Assert.*;

public class TddCourseTest {

    private static Logger LOGGER = Logger.getLogger(TddCourseTest.class.getCanonicalName());

    @Test
    public void testIsTddCourse(){
        LOGGER.info("Testing is tdd course");
        assertTrue(TddCourse.isTddTCourse());
    }

}