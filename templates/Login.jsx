import { Link } from "react-router-dom";
import styles from "./LogIn.module.css";

export const LogIn = () => {
  return (
    <div className={styles.wrapper}>
      <Link to="/" className={styles.logo}>
        <img src="/Logo Icon.svg" alt="Логотип" className={styles.logo_img} />
        <img
          src="/CENTER TKANI.svg"
          alt="Название"
          className={styles.logo_text}
        />
      </Link>

      <div className={styles.form}>
        <h3>Войти</h3>
        <div className={styles.form_email}>
          <p>Электронная почта</p>
          <input
            type="email"
            name="email"
            id="email"
            placeholder="user@company.com"
            required
            className={styles.form_input}
          />
        </div>
        <div className={styles.form_password}>
          <div className={styles.form_password_link}>
            <p>Пароль</p>
            <Link to="/forgot">Забыли пароль?</Link>
          </div>
          <input
            type="password"
            name="password"
            id="password"
            placeholder="Пароль"
            required
            className={styles.form_input}
          />
        </div>
        <button type="submit" className={styles.form_btn}>Войти</button>
        <div className={styles.form_link}>
          <p>Нет аккаунта?</p>
          <Link to="/sing_up" className={styles.form_link_singUp}>
            Зарегистрируйтесь
          </Link>
        </div>
      </div>
    </div>
  );
};