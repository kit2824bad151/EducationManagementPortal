import { useState } from "react";
import "./App.css";

const menuItems = [
  { name: "Dashboard", icon: "▦" },
  { name: "Profile", icon: "♙" },
  { name: "My Courses", icon: "▣" },
  { name: "Assignments", icon: "📝" },
  { name: "Attendance", icon: "✓" },
  { name: "Examinations", icon: "▤" },
  { name: "Grades", icon: "★" },
  { name: "Progress", icon: "↗" },
  { name: "AI Recommendations", icon: "🤖" }
];

function Login({ onLogin }) {
  return (
    <div className="login-page">

      <div className="login-card">

        <div className="login-image">
          <div className="graduation">🎓</div>
          <div className="book book1"></div>
          <div className="book book2"></div>
          <div className="book book3"></div>
          <div className="plant">🌱</div>
        </div>

        <div className="login-form">

          <h1>
            <span>EduAI</span> Portal
          </h1>

          <p className="subtitle">
            Academic Intelligence Platform
          </p>

          <input
            type="email"
            placeholder="Email"
          />

          <input
            type="password"
            placeholder="Password"
          />

          <button
            className="student-btn"
            onClick={() => onLogin("student")}
          >
            👤 &nbsp; Login as Student
          </button>

          <button
            className="teacher-btn"
            onClick={() => onLogin("teacher")}
          >
            👨‍🏫 &nbsp; Login as Teacher
          </button>

          <button
            className="admin-btn"
            onClick={() => onLogin("admin")}
          >
            🛡️ &nbsp; Login as Admin
          </button>

          <p className="copyright">
            © 2026 EduAI Portal. All rights reserved.
          </p>

        </div>
      </div>

    </div>
  );
}


function Sidebar({ activePage, setActivePage, role, logout }) {

  return (
    <aside className="sidebar">

      <div className="brand">
        🎓 <span>EduAI</span>
      </div>

      <div className="role-name">
        {role === "student" ? "Student Portal" : "Academic Portal"}
      </div>

      <nav>

        {menuItems.map((item) => (

          <button
            key={item.name}
            className={
              activePage === item.name
                ? "menu-item active"
                : "menu-item"
            }
            onClick={() => setActivePage(item.name)}
          >

            <span className="menu-icon">
              {item.icon}
            </span>

            {item.name}

          </button>

        ))}

      </nav>

      <button
        className="logout"
        onClick={logout}
      >
        ⇥ &nbsp; Logout
      </button>

    </aside>
  );
}


function Navbar({ activePage }) {

  return (
    <header className="navbar">

      <h2>{activePage}</h2>

      <div className="user-area">

        <span className="notification">
          🔔
        </span>

        <div className="avatar">
          S
        </div>

        <span>
          Student
        </span>

        <span>⌄</span>

      </div>

    </header>
  );
}


function StatCard({ title, value, icon, status }) {

  return (
    <div className="stat-card">

      <div>
        <p>{title}</p>

        <h2>{value}</h2>

        <small>
          {status}
        </small>
      </div>

      <div className="stat-icon">
        {icon}
      </div>

    </div>
  );
}


function PerformanceChart() {

  const marks = [65, 75, 72, 85, 90];

  return (
    <div className="performance-card">

      <h3>Performance Trend</h3>

      <div className="chart">

        <div className="y-axis">
          <span>100</span>
          <span>80</span>
          <span>60</span>
          <span>40</span>
        </div>

        <div className="chart-area">

          <div className="grid-line"></div>
          <div className="grid-line"></div>
          <div className="grid-line"></div>
          <div className="grid-line"></div>

          <div className="bars">

            {marks.map((mark, index) => (

              <div
                className="bar-container"
                key={index}
              >

                <div
                  className="bar"
                  style={{
                    height: `${mark * 2}px`
                  }}
                ></div>

                <span>
                  {["Jan", "Feb", "Mar", "Apr", "May"][index]}
                </span>

              </div>

            ))}

          </div>

        </div>

      </div>

    </div>
  );
}


function AIInsight() {

  return (
    <div className="ai-card">

      <div className="ai-title">

        <h3>🤖 AI Academic Insight</h3>

        <span className="risk">
          Medium Risk
        </span>

      </div>

      <div className="ai-stats">

        <div>
          <p>Risk Score</p>
          <strong>62</strong>
          <span>/100</span>
        </div>

        <div>
          <p>Weak Subjects</p>
          <strong className="subjects">
            Physics, Statistics
          </strong>
        </div>

      </div>

      <h4>Recommendations</h4>

      <ul>

        <li>
          <span>✓</span>
          Improve Physics practice
        </li>

        <li>
          <span>✓</span>
          Complete pending assignments
        </li>

        <li>
          <span>✓</span>
          Maintain attendance above 80%
        </li>

      </ul>

    </div>
  );
}


function Dashboard() {

  return (
    <>
      <div className="welcome">

        <h1>
          Welcome back, Student 👋
        </h1>

        <p>
          Here's your academic overview.
        </p>

      </div>

      <div className="stats-grid">

        <StatCard
          title="GPA"
          value="8.2"
          status="Good"
          icon="◉"
        />

        <StatCard
          title="Attendance"
          value="86%"
          status="Good"
          icon="▣"
        />

        <StatCard
          title="Courses"
          value="6"
          status="Enrolled"
          icon="▤"
        />

        <StatCard
          title="Pending Assignments"
          value="2"
          status="Pending"
          icon="📝"
        />

      </div>

      <div className="dashboard-grid">

        <PerformanceChart />

        <AIInsight />

      </div>
    </>
  );
}


function Profile() {

  return (
    <div className="page-card">

      <h1>Student Profile</h1>

      <div className="profile-box">

        <div className="big-avatar">
          S
        </div>

        <div>
          <h2>Student</h2>
          <p>student@eduai.com</p>
          <p>B.Tech Artificial Intelligence and Data Science</p>
        </div>

      </div>

      <div className="info-grid">

        <div>
          <label>Student ID</label>
          <p>EDU2026001</p>
        </div>

        <div>
          <label>Department</label>
          <p>AI & Data Science</p>
        </div>

        <div>
          <label>Year</label>
          <p>3rd Year</p>
        </div>

        <div>
          <label>Academic Status</label>
          <p className="good">Active</p>
        </div>

      </div>

    </div>
  );
}


function Courses() {

  const courses = [
    ["Artificial Intelligence", "AI301", "92%"],
    ["Machine Learning", "ML302", "88%"],
    ["Data Science", "DS303", "85%"],
    ["Cloud Computing", "CC304", "90%"],
    ["Deep Learning", "DL305", "82%"],
    ["Software Engineering", "SE306", "87%"]
  ];

  return (
    <div className="page-card">

      <h1>My Courses</h1>

      <div className="course-grid">

        {courses.map((course) => (

          <div className="course-card" key={course[1]}>

            <div className="course-icon">
              📚
            </div>

            <h3>{course[0]}</h3>

            <p>{course[1]}</p>

            <div className="progress-bg">
              <div
                className="progress-fill"
                style={{
                  width: course[2]
                }}
              ></div>
            </div>

            <small>
              Attendance {course[2]}
            </small>

          </div>

        ))}

      </div>

    </div>
  );
}


function Assignments() {

  return (
    <div className="page-card">

      <h1>Assignments</h1>

      <div className="assignment-list">

        <div className="assignment">
          <div>
            <h3>Machine Learning Project</h3>
            <p>Due: 20 August 2026</p>
          </div>
          <span className="pending">Pending</span>
        </div>

        <div className="assignment">
          <div>
            <h3>AI Research Paper</h3>
            <p>Due: 25 August 2026</p>
          </div>
          <span className="submitted">Submitted</span>
        </div>

        <div className="assignment">
          <div>
            <h3>Cloud Computing Lab</h3>
            <p>Due: 28 August 2026</p>
          </div>
          <span className="pending">Pending</span>
        </div>

      </div>

    </div>
  );
}


function Attendance() {

  return (
    <div className="page-card">

      <h1>Attendance</h1>

      <div className="attendance-big">
        86%
        <span>Overall Attendance</span>
      </div>

      <div className="attendance-list">

        <p>
          Artificial Intelligence
          <strong>92%</strong>
        </p>

        <p>
          Machine Learning
          <strong>88%</strong>
        </p>

        <p>
          Data Science
          <strong>85%</strong>
        </p>

        <p>
          Cloud Computing
          <strong>90%</strong>
        </p>

      </div>

    </div>
  );
}


function Examinations() {

  return (
    <div className="page-card">

      <h1>Examinations</h1>

      <div className="exam-card">
        <h3>Machine Learning</h3>
        <p>Internal Examination</p>
        <strong>28 August 2026</strong>
      </div>

      <div className="exam-card">
        <h3>Artificial Intelligence</h3>
        <p>Semester Examination</p>
        <strong>05 September 2026</strong>
      </div>

    </div>
  );
}


function Grades() {

  return (
    <div className="page-card">

      <h1>Grades</h1>

      <div className="grade-table">

        <div className="grade-row header">
          <span>Subject</span>
          <span>Grade</span>
          <span>Score</span>
        </div>

        <div className="grade-row">
          <span>Artificial Intelligence</span>
          <b>A+</b>
          <span>92</span>
        </div>

        <div className="grade-row">
          <span>Machine Learning</span>
          <b>A</b>
          <span>88</span>
        </div>

        <div className="grade-row">
          <span>Data Science</span>
          <b>A</b>
          <span>85</span>
        </div>

        <div className="grade-row">
          <span>Cloud Computing</span>
          <b>A+</b>
          <span>90</span>
        </div>

      </div>

    </div>
  );
}


function Progress() {

  return (
    <div className="page-card">

      <h1>Academic Progress</h1>

      <div className="progress-main">

        <div>
          <h2>Overall Progress</h2>

          <div className="circle-progress">
            82%
          </div>

        </div>

        <div className="progress-details">

          <p>
            Semester Progress
            <strong>78%</strong>
          </p>

          <p>
            Course Completion
            <strong>85%</strong>
          </p>

          <p>
            Assignment Completion
            <strong>80%</strong>
          </p>

        </div>

      </div>

    </div>
  );
}


function AIRecommendations() {

  return (
    <div className="page-card">

      <h1>AI Recommendations 🤖</h1>

      <div className="recommendation-card">
        <h3>📘 Focus on Physics</h3>
        <p>
          Your recent performance indicates that
          additional Physics practice could improve
          your overall academic score.
        </p>
      </div>

      <div className="recommendation-card">
        <h3>📝 Complete Assignments</h3>
        <p>
          You currently have 2 pending assignments.
          Completing them can improve your academic progress.
        </p>
      </div>

      <div className="recommendation-card">
        <h3>📅 Maintain Attendance</h3>
        <p>
          Your current attendance is 86%.
          Continue maintaining regular attendance.
        </p>
      </div>

    </div>
  );
}


function App() {

  const [loggedIn, setLoggedIn] = useState(false);

  const [role, setRole] = useState("student");

  const [activePage, setActivePage] = useState("Dashboard");


  const login = (selectedRole) => {

    setRole(selectedRole);
    setLoggedIn(true);
    setActivePage("Dashboard");

  };


  const logout = () => {

    setLoggedIn(false);
    setActivePage("Dashboard");

  };


  if (!loggedIn) {

    return (
      <Login onLogin={login} />
    );

  }


  const renderPage = () => {

    switch (activePage) {

      case "Profile":
        return <Profile />;

      case "My Courses":
        return <Courses />;

      case "Assignments":
        return <Assignments />;

      case "Attendance":
        return <Attendance />;

      case "Examinations":
        return <Examinations />;

      case "Grades":
        return <Grades />;

      case "Progress":
        return <Progress />;

      case "AI Recommendations":
        return <AIRecommendations />;

      default:
        return <Dashboard />;

    }

  };


  return (

    <div className="app">

      <Sidebar
        activePage={activePage}
        setActivePage={setActivePage}
        role={role}
        logout={logout}
      />

      <main className="main">

        <Navbar
          activePage={activePage}
        />

        <section className="content">

          {renderPage()}

        </section>

      </main>

    </div>

  );
}

export default App;